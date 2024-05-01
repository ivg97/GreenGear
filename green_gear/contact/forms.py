from django import forms
from contact.models import CommunicationService


class CommunicationServiceForm(forms.ModelForm):
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
        fields = ('subject', 'email', 'message')

