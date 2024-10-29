from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, EditProfileForm, EditProfileExtraForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
    
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # ログイン後のリダイレクト先を指定
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = EditProfileExtraForm(request.POST, instance=request.user.profile)
        
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, 'プロフィールが更新されました！')
            return redirect('profile')  # プロフィールページにリダイレクト
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = EditProfileExtraForm(instance=request.user.profile)
    
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'edit_profile.html', context)