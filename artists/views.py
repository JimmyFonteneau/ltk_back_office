from django.shortcuts import render, redirect
from .forms import ArtistForm, ModifyArtistForm
from .models import Artist
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from artworks.models import Artwork

def is_superuser(user=None):    
    if user == None:
        return false   
    return user.is_superuser

@user_passes_test(is_superuser)
def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect("artists:artists")
    else:
        form = ArtistForm()
    return render(request, 'artists/artists_edit.html', {'form': form})

@user_passes_test(is_superuser)
def update_artist(request, artist_id):             
    artist = Artist.objects.get(id=artist_id)    
    if request.method == 'POST':
        if 'delete_artist' in request.POST:
            artist.delete()                    
            return redirect("artists:artists")
        else:
            form = ModifyArtistForm(request.POST, instance=artist)
            if form.is_valid():           
                form.save()
                return redirect("artists:artists")
    else:
        form = ModifyArtistForm(instance=artist)
    return render(
        request,
        'artists/artist_update.html',
        {
            'form': form,
        }
    ) 

def all_artists(request):
    artists_list = Artist.objects.all()
    paginator = Paginator(artists_list, 5)
    page = request.GET.get('page')
    artists = paginator.get_page(page)
    if request.user.is_superuser:
        return render(
            request,
            'artists/artists_list_admin.html',
            {
                'artists_list': artists,
            }
        )
    else:
        return render(
            request,
            'artists/artists_list.html',
            {
                'artists_list': artists,
            }
        )

def artist(request, artist_id):             
    artist = Artist.objects.get(id=artist_id)    
    artworks = Artwork.objects.filter(artist_id=artist_id)[:4]   
    return render(
        request,
        'artists/artist.html',
        {
            'artist': artist,
            'artworks': artworks,
        }
    ) 
