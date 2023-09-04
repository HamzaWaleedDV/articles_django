from django import forms
from myapp.models import Authors
from myapp.models import Tag, Article


field_attrs = {'class': 'form-control mb-2'}


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'tags']
        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'content': forms.Textarea(attrs=field_attrs),
            'author': forms.Select(attrs=field_attrs),
            'tags': forms.SelectMultiple(attrs=field_attrs),
        }



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['name', 'email', 'birthdate', 'bio']
        widgets = {
            'name': forms.TextInput(attrs=field_attrs),
            'email': forms.TextInput(attrs=field_attrs),
            'birthdate': forms.TextInput(attrs=field_attrs),
            'bio': forms.Textarea(attrs=field_attrs),
        }