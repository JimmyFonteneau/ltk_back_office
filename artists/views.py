from django.shortcuts import render, redirect
from .forms import ArtistForm
from .models import Artist

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

def all_artists(request):
    artists = Artist.objects.all()
    return render(
        request,
        'artists/artists_list.html',
        {
            'artists_list': artists,
        }
    )