from django import forms
from about_us.models import Feedback


class FeedbackForm(forms.ModelForm):
    assessment = forms.IntegerField(
        label='Assessment',
    )
    feedback = forms.CharField(
        label='Feedback',
        widget=forms.Textarea
    )

    class Meta:
        model = Feedback
        fields = ('assessment', 'feedback')


