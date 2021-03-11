from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Profile
        field = ['__all__']
        exclude = ['slug']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'type',
                    'placeholder': 'Fullname'

                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'type',
                    'placeholder': 'Phone Number'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'type',
                    'placeholder': 'Email'
                }
            ),

            'address': forms.TextInput(
                attrs={
                    'class': 'type',
                    'placeholder': 'Address'
                }
            ),

            'relation': forms.TextInput(
                attrs={
                    'class': 'type',
                    'placeholder': 'Relation'
                }
            ),
        }