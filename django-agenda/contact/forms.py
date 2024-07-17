from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


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
                    'accept': 'image/*',
                    'required' : False
                },
                
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
            }),
            
        }

class UpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1
