from django import forms

from blog.models import NewPostEmail


class NewPostEmailForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput
        (attrs={'placeholder': 'Enter your email'})
    )

    class Meta:
        model = NewPostEmail
        fields = ['email']
