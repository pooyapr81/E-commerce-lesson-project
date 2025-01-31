from .models import Article
from django import forms


class formcreatupdate(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('summery', 'Author','master',)


class ArticleSearchForm(forms.Form):
    search = forms.CharField()
