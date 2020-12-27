from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        return redirect('/success')


def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.filter(email = request.POST['email'):
        return redirect('/')
    else:
        user = User.objects.filter(email = email)[0]
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            messages.success(request, "You have successfully logged in!")
        else:
            messages.error(request, "Incorrect email or password")
    return redirect('/success')


def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)



def logout(request):
    request.session.clear()
    return redirect('/')