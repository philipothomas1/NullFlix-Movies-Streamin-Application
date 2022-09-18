from django import forms
from .models import Review, RATE_CHOICES,Movie

class RateForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form__textarea'}), required=False)
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

	class Meta:
		model = Review
		fields = ('text', 'rate')

class MovieSearchForm(forms.ModelForm):
   
    class Meta:
        model = Movie
        fields = ['Title']