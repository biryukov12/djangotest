from django import forms


class EmailArticleFrom(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'md-form'}))
    email_from = forms.EmailField(widget=forms.TextInput(attrs={'class': 'md-form'}))
    email_to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'md-form'}))
