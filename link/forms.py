from django import forms

from .models import Category, Link


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('category', 'name', 'description', 'url',)