from django.shortcuts import render, redirect
from .forms import ArtworkForm, ModifyArtworkForm
from .models import Artwork
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail

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
    return render(
        request, 
        'artworks/artworks_list.html', 
        {
            'artworks': artworks
        }
    )

def artwork(request, artwork_id):             
    artwork = Artwork.objects.get(id=artwork_id)    
    return render(
        request,
        'artworks/artwork.html',
        {
            'artwork': artwork,
        }
    )  
