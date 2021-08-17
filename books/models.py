from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('Author', related_name='authors')
    description= models.CharField(max_length=255)
    book_url =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=False)
    # add ManyToManyField for categories

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=225)
    books = models.ManyToManyField(Book, related_name='book')

    class Meta:
        ordering = ['name']
        
    
    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75, null=True)

    def __str__(self):
        return self.category_name