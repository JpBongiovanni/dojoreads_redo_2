from django.db import models
from django.db import models
from registration_app.models import User


class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.IntegerField()
    poster = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    contributor = models.ForeignKey(User, related_name = "book_added", on_delete = models.CASCADE)
    review = models.ForeignKey(Review, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    name = models.CharField(max_length=255)
    book_written = models.OneToOneField(Book, on_delete = models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)