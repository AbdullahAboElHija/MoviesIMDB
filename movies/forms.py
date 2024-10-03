from django import forms
from .models import Movie

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['author']  # This will remove the author field from the form
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),  # Set the input type to date
        }

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']  # Only include the content field
