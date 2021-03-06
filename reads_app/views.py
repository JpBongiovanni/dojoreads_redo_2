from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Book, Author, Review
from registration_app.models import User

def index(request):

    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "recent_reviews": Review.objects.all().order_by('-created_at')[0:3],
        "books": Book.objects.all()
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
        "book": Book.objects.get(id = book_id)
    }
    return render(request, 'book_info.html', context)

def user_info_page(request, contributor_id):
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "review_contributor": User.objects.get(id = contributor_id),
        "books_contributed": User.objects.get(id = contributor_id).book_added.all()
    }
    return render(request, 'user_info.html', context)

def add_book_and_review(request):
    errors = User.objects.validate(request.POST)
    
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/reads')
    else:
        Author.objects.create(
            name = request.POST['name'],
        )
        
    latest_author = Author.objects.last()

    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/reads')
    else:
        Book.objects.create(
            title = request.POST['title'],
            contributor = User.objects.get(id = request.session['user_id']),
            author = latest_author
        )

    latest_book = Book.objects.last()

    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/reads')
    else:
        Review.objects.create(
            content = request.POST['content'],
            rating = request.POST['rating'],
            poster = User.objects.get(id = request.session['user_id']),
            book = latest_book
    )

    return redirect('/reads')

def delete_book(request, book_id):
    book = Book.objects.get(id = book_id)
    if book.contributor.id == request.session['user_id']:
        book.delete()
    return redirect('/reads')
    
def add_user_review(request, book_id):
    Review.objects.create(
        content = request.POST['content'],
        rating = request.POST['rating'],
        poster = User.objects.get(id = request.session['user_id']),
        book = Book.objects.get(id = book_id)
    )
    return redirect(f'/reads/{book_id}')