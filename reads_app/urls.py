from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book_page),
    path('reads/add', views.add_book_and_review),
    path('reads/<int:book_id>/delete', views.delete_book),
    path('reads/<int:book_id>/', views.book_info_page),
    path('reads/add_review', views.add_user_review)
]