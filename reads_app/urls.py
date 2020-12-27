from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reads', views.add_book_page),
    path('reads/add', views.add_book_and_review),
    path('reads/<int:book_id>/delete', views.delete_book),
]