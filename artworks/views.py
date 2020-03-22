from django.shortcuts import render, redirect
from .forms import ArtworkForm
from .models import Artwork

def artwork_new(request):
    if request.method == "POST":
        form = ArtworkForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect("artworks:artworks_list")
    else:
        form = ArtworkForm()
    return render(request, 'artworks/artwork_new.html', {'form': form})

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
