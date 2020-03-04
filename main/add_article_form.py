from django import forms
from main.models import Article
from datetime import datetime


class AddArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)
        self.fields['publish'].initial = datetime.now().strftime('%d.%m.%Y %H:%M')

    class Meta:
        model = Article
        fields = ('title', 'author', 'body', 'publish', 'status')
        labels = {
            'body': 'Text',
            'publish': 'Time to publish'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'md-form'}),
            'author': forms.TextInput(attrs={'class': 'md-form'}),
            'body': forms.Textarea(attrs={'class': 'md-textarea', 'rows': 3}),
            'publish': forms.DateTimeInput(attrs={'class': 'md-form'}),
            'status': forms.Select(attrs={'class': 'custom-select'})

        }
