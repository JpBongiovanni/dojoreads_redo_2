from django.db import models
from registration_app.models import User
import re
import bcrypt

class BookManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['name']) < 2:
            errors['name'] = 'Author name must be at least 2 characters and no more than 30 characters'
        
        if len(form['title']) < 2:
            errors['title'] = 'Book title must be at least 2 characters'

        if len(form['content']) < 2:
            errors['content'] = 'Review name must be at least 10 characters'
        
        return errors

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = BookManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    contributor = models.ForeignKey(User, related_name = "book_added", on_delete = models.CASCADE)
    author = models.ForeignKey(Author, related_name = "book_written", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = BookManager()

class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.IntegerField()
    poster = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = BookManager()