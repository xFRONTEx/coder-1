from django import forms
from core.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['nombre', 'calificacion', 'mensaje', 'opinion']
        