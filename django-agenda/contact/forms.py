from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','last_name','phone','email','description','category', 'picture')
        widgets = {
            'name': forms.TextInput(
                #atributos 
                attrs={
                    'class':'tese',
                    'placeholder': 'Nome'
                }
            ),
            'picture' : forms.FileInput(
                attrs={
                    'accept': 'image/*'
                }
            )
        }
    def clean(self):
        name = self.cleaned_data.get("name")
        last_name = self.cleaned_data.get('last_name')

        if name == last_name:
            self.add_error(
                'last_name',
                ValidationError("O nome não deve ser igual ao seugndo",code='invalid')
            )


        return super().clean()
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise ValidationError("Nome muito curto",code='invalid')
        
        return name

#UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name','last_name','email','username','password1','password2'
        )
        widgets = {
            'first_name' : forms.TextInput(
            attrs = {
                'required': True
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            self.add_error(
                'email',
                ValidationError(
                    "Este email já esta registrado",
                    code='invalid'
                )
            )

        return email

