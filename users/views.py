from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, AccountSettingsForm
from .models import UserProfile


def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:myaccount"))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['raw_password']
            user = UserProfile.objects.create_user(
                username=username,
                email=email,
                password=raw_password,
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("users:myaccount"))
    else:
        form = RegisterForm()
    return render(
        request,
        'users/register.html',
        {
            'url_form': reverse("users:register"),
            'title': "Inscription",
            'form':form,
        }
    )


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("artworks:artworks_list"))
    elif 'username' in request.POST and 'password' in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse("artworks:artworks_list"))
            else:
                return render(
                    request,
                    'users/login.html',
                    {
                        "auth_error": True,
                        'form':form,
                    }
                )
    else:
        form = LoginForm()
        return render(
            request,
            'users/login.html',
            {
                'form':form,
            }
        )


@login_required
def myaccount(request):
    return render(
        request,
        'users/myaccount.html',
        )


@login_required
def account_settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:myaccount"))
    else:
        form = AccountSettingsForm(instance=request.user)
        return render(
            request,
            'users/register.html',
            {
                'url_form': reverse("users:account_settings"),
                'title': "Modification du compte",
                'form':form,
                'modify': True
            }
        )