from django import forms
from contact.models import CommunicationService


class CommunicationServiceForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput()
    )
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput()
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(),
    )

    class Meta:
        model = CommunicationService
        fields = ('full_name', 'subject', 'email', 'message')

