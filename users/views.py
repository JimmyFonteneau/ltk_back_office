from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, AccountSettingsForm, ForgotPassword, UpdatedPassword
from .models import UserProfile
from orders.models import Order, OrderArtworkRate
from django.core.mail import send_mail
from django.conf import settings

def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:myaccount"))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
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
        return HttpResponseRedirect(reverse("users:myaccount"))
    elif 'email' in request.POST and 'password' in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                next_url = request.GET.get('next')
                login(request, user)
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return HttpResponseRedirect(reverse("users:myaccount"))
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

@login_required
def myorders(request):
    orders = Order.objects.filter(user=request.user)

    for order in orders:
        order_artwork_rates = OrderArtworkRate.objects.filter(order=order)

        order.artworks = []
        for order_artwork_rate in order_artwork_rates:
            order.artworks.append(order_artwork_rate.artwork)

    return render(
        request,
        'users/myorders.html',
        {
            'orders': orders
        }
    )

def all_users(request):
    users = UserProfile.objects.all()
    if request.user.is_superuser:        
        return render(
            request,
            'users/users_list.html',
            {
                'users_list': users
            }
        )
    else:
        return HttpResponseRedirect(reverse("users:myaccount"))

def user(request, user_id):             
    user = UserProfile.objects.get(id=user_id)    
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=user)
        if form.is_valid():           
            form.save()
            return HttpResponseRedirect(reverse("users:users_all"))
    else:
        form = AccountSettingsForm(instance=user)
    return render(
        request,
        'users/user_update.html',
        {
            'form': form,
        }
    ) 

def forgot_password(request):                    
    if request.method == 'POST':
        form = ForgotPassword(request.POST)        
        if form.is_valid():           
            user = UserProfile.objects.get(email=form.cleaned_data['email'])            
            user.updated_password = True
            user.save()
            send_mail(
                'Demande de récupération de mot de passe',
                '<a href="'+settings.ALLOWED_HOSTS[1]+'users/updated-password-'+str(user.id)+'">Modifier mon mot de passe</a>',
                form.cleaned_data['email'],
                ['admin@email.com'],
                fail_silently=False,
            )
    else:
        form = ForgotPassword()
    return render(
        request,
        'users/forgot_password.html',
        {
            'form': form,
        }
    ) 

   
def updated_password (request, user_id):                         
    user = user = UserProfile.objects.get(id=user_id) 
    if user.updated_password == False:
        return HttpResponse('Action non autorisée, l\'utilisateur n\'a pas demandé de modification de mot de passe')
    if request.method == 'POST':
        form = UpdatedPassword(request.POST)        
        if form.is_valid():           
            user.set_password(form.cleaned_data['raw_password'])
            user.updated_password = False
            user.save()
            return render(
                request,
                'users/password_validate.html',
            )   
    else:
        form = UpdatedPassword()
    return render(
        request,
        'users/updated_password.html',
        {
            'form': form,
            'url_form': reverse('users:updated_password', kwargs={'user_id': str(user_id) }),
        }
    ) 