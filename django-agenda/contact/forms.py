from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms


#form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','last_name','phone','description',)
        widgets = {
            'name': forms.TextInput(
                #atributos 
                attrs={
                    'class':'tese',
                    'placeholder': 'Nome'
                }
            )
        }
    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            'name', ValidationError('Nome inválido',code='invalid')
        )
        #non_errors
        self.add_error(
            None, ValidationError('Error',code='invalid')
        )

        return super().clean()
    
