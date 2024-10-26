from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.urls import reverse

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # ログイン後のリダイレクト先を指定
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})