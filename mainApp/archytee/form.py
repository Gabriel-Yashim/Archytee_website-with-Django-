from django import forms
from .models import ClientForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ClientForm
        fields = ['name', 'phone', 'email', 'message']