from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
