from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=25, help_text="Имя автора")
    email = models.EmailField(help_text='Email автора')

    def __str__(self):
        return f' {self.name} | {self.email}'


class Category(models.Model):
    name = models.CharField(max_length=25, help_text='Название категории')

    def __str__(self):
        return self.name




class Recipe(models.Model):
    name = models.CharField(max_length=25, help_text='Название рецепта')
    description = models.TextField(help_text='Описание рецепта')
    stages = models.TextField(help_text='Шаги приготовления')
    time = models.CharField(max_length=10, help_text='Время приготовления')
    image = models.ImageField(upload_to='media', default='no_image')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def short_desc(self):
        desc = self.description[:25]
        return f' {desc}...'
