
from django import forms

class CowAddForm(forms.Form):
    what_does_the_cowsay = forms.CharField(max_length=142)


