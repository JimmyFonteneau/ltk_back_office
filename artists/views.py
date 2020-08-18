import csv, io
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
        form = ArtistForm(request.POST, request.FILES)
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
            form = ModifyArtistForm(request.POST, request.FILES, instance=artist)
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

def artist_upload(request):
    template = "artists/import_artists.html"
    prompt = {
        'artist': 'Order of the csv should be , firstname, lastname, name, artist_description, artist_universe'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Artist.objects.update_or_create(
            firstname=column[0],
            lastname=column[1],
            name=column[2],
            artist_description=column[3],
            artist_universe=column[4],
        )
    context = {}
    return redirect("artists:artists")
