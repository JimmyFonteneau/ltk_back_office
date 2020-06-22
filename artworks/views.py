from django.shortcuts import render, redirect
from .forms import ArtworkForm, ModifyArtworkForm, StyleForm
from .models import Artwork, Artwork_Style
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from carts.forms import CartAddArtworkForm
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse

def is_superuser(user=None):    
    if user == None:
        return false   
    return user.is_superuser

@user_passes_test(is_superuser)
def artwork_new(request):
    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()           
            send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
            return redirect("artworks:artworks_list")
    else:
        form = ArtworkForm()
    return render(request, 'artworks/artwork_new.html', {'form': form})

@user_passes_test(is_superuser)
def update_artwork(request, artwork_id):             
    artwork = Artwork.objects.get(id=artwork_id)    
    if request.method == 'POST':
        form = ModifyArtworkForm(request.POST, instance=artwork)
        if form.is_valid():           
            form.save()
    else:
        form = ModifyArtworkForm(instance=artwork)
    return render(
        request,
        'artworks/artwork_update.html',
        {
            'form': form,
        }
    ) 

def artworks_list(request):    
    artworks = Artwork.objects.all()
    styles = Artwork_Style.objects.all()
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:       
        if int(url_parameter) > 0:
            artworks = Artwork.objects.filter(style=url_parameter)
    
    ctx["artworks"] = artworks

    if request.user.is_superuser:
        if request.is_ajax():
            html = render_to_string(
                template_name="artworks/artworks_filtered.html", 
                context={"artworks": artworks}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)
        return render(
            request, 
            'artworks/artworks_list_admin.html', 
            {
                'artworks': artworks,
                'styles': styles,
            }
        )
    else :
        return render(
            request, 
            'artworks/artworks_list.html', 
            {
                'artworks': artworks
            }
        )

def artwork(request, artwork_id):             
    artwork = Artwork.objects.get(id=artwork_id)
    cart_artwork_form = CartAddArtworkForm()
    return render(
        request,
        'artworks/artwork.html',
        {
            'artwork': artwork,
            'cart_artwork_form': cart_artwork_form
        }
    )

def add_style(request):
    if request.method == "POST":
        form = StyleForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect("artworks:artworks_list")
    else:
        form = StyleForm()
    return render(request, 'artworks/add_style.html', {'form': form})