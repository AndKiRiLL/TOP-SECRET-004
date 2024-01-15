from django import forms
from .models import Category, Author, Post

class FormCreate(forms.Form):
    name = forms.CharField(required=True, label="", max_length=150, widget=forms.Textarea(attrs={'class':'main__create__block__textarea', 'name': 'name'}))
    image = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'main__create__block__input', 'name': 'image'}))
    date = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'main__create__block__input', 'name': 'date'}))

    categories = Category.objects.all().values_list()
    categories_news = []
    for i in range(0, len(categories)):
        categories_news.append((categories[i][0], categories[i][1]))

    category = forms.ChoiceField(choices=(categories_news), required=True, label="", widget=forms.Select(attrs={'class':'main__create__block__select', 'name': 'category'}))

    authors = Author.objects.all().values_list()
    authors_news = []
    for i in range(0, len(authors)):
        authors_news.append((authors[i][0], authors[i][2] + ' ' + authors[i][1]))

    author = forms.ChoiceField(choices=(authors_news), required=True, label="", widget=forms.Select(attrs={'class':'main__create__block__select', 'name': 'author'}))


class FormEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'name': forms.Textarea(attrs={'class': 'main__create__block__textarea'}),
            'img': forms.TextInput(attrs={'class': 'main__create__block__input'}),
            'date': forms.TextInput(attrs={'class': 'main__create__block__input'}),
            'category': forms.Select(attrs={'class': 'main__create__block__select'}),
            'author': forms.Select(attrs={'class': 'main__create__block__select'}),
        }
