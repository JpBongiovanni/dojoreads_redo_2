from django.db import models
from registration_app.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    contributor = models.ForeignKey(User, related_name = "book_added", on_delete = models.CASCADE)
    author = models.ForeignKey(Author, related_name = "book_written", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.IntegerField()
    poster = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)