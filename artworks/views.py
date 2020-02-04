from django.shortcuts import render

from .models import Artwork

def artworks_list(request):
    artworks = Artwork.objects.filter()
    return render(
        request, 
        'artworks/artworks_list.html', 
        {
            'artworks': artworks
        }
    )
