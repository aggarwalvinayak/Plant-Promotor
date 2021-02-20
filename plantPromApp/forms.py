from django import forms
from .models import plantPromModel

class plantPromForm(forms.ModelForm):
    Sentence = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    class Meta:
        model = plantPromModel
        fields = [
            'Sentence'
        ]