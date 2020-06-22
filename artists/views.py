from django.shortcuts import render, redirect
from .forms import ArtistForm, ModifyArtistForm
from .models import Artist
from django.contrib.auth.decorators import login_required, user_passes_test

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
            # return redirect('post_detail', pk=post.pk)
            return redirect("users:account_settings")
    else:
        form = ArtistForm()
    return render(request, 'artists/artists_edit.html', {'form': form})

@user_passes_test(is_superuser)
def update_artist(request, artist_id):             
    artist = Artist.objects.get(id=artist_id)    
    if request.method == 'POST':
        form = ModifyArtistForm(request.POST, instance=artist)
        if form.is_valid():           
            form.save()
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
    artists = Artist.objects.all()
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
    return render(
        request,
        'artists/artist.html',
        {
            'artist': artist,
        }
    ) 