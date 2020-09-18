from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from .models import Examinee, Examiner
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/dashboard')

    context = {
        'form': form,
    }
    return render(request, "UserManagement/login.html", context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/dashboard')

    context = {
        'form': form,
    }
    return render(request, "UserManagement/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def user_dash(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user}

        return render(request, 'UserManagement/user_dash_base.html', context)
    else:
        return redirect('/')

def show_all_user(request):
    examinee = Examinee.objects.all()
    examiner = Examiner.objects.all()
    context = {
        'examiner': examiner,
        'examinee': examinee
    }
    return render(request, 'UserManagement/show_all_user.html', context)