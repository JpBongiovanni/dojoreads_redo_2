from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Book, Author, Review
from registration_app.models import User

def index(request):
    
            
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "book": Book.objects.all(),
        "review": Book.objects.get(pk=1).book_reviews.all()
    }
    return render(request, "books_home.html", context)

def add_book_page(request):
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "author": Author.objects.all(),
    }
    return render(request, "add_book_review.html", context)

def book_info_page(request, book_id):
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "book": Book.objects.get(id = book_id),
    }
    return render(request, 'book_info.html', context)

def add_book_and_review(request):
    
    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        poster = User.objects.get(id = request.session['user_id']),
        
    )
    latest_review = Review.objects.last()
    

    Book.objects.create(
        title = request.POST['title'],
        contributor = User.objects.get(id = request.session['user_id']),
        review = latest_review,
    )

    latest_book = Book.objects.last()

    Author.objects.create(
        name = request.POST['name'],
        book_written = latest_book,
    )
    return redirect('/reads')


def delete_book(request, book_id):
    book = Book.objects.get(id = book_id)
    if book.contributor.id == request.session['user_id']:
        book.delete()
    return redirect('/reads')
    
def add_user_review(request):
    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        poster = User.objects.get(id = request.session['user_id']),
    )
    return redirect(f'reads/{{Book.id}}')