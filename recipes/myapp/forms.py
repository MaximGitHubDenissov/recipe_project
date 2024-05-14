from django import forms
from .models import Category


class RecipeForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Выберите категорию")
    name = forms.CharField(max_length=25, label='Название рецепта')
    description = forms.CharField(label='Описание рецепта', max_length=200,
                                  widget=forms.Textarea(attrs={'placeholder': 'Описание рецепта'}))
    stages = forms.CharField(label='Этапы приготовления', max_length=200,
                             widget=forms.Textarea(attrs={'placeholder': 'Этапы приготовления'}))
    time = forms.CharField(label='Время приготовления', max_length=10)
    image = forms.ImageField(label='Загрузите фото рецепта')


