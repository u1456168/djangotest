from django import forms
from hotel.models import Category , Page
class Catform(forms.ModelForm):
    class Meta:
        model = Category;
        fields = ['name'];
