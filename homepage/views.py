from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView
from artworks.models import Artwork
from django.db.models import Q
from artists.models import Artist
from orders.models import Order, OrderArtworkRate
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from django.utils.timezone import make_aware

def homepage(request):
    artworks = Artwork.objects.all()
    artworks = artworks.filter(spotlight=True)
    artist = Artist.objects.filter(spotlight=True).first()
    return render(
        request, 
        'homepage/homepage.html',
        {
            'artworks': artworks,
            'artist': artist,
        }       
    )

def dashboard(request):
    order = Order.objects.filter(state=1).count()
    artworks = Artwork.objects.all().count()
    artworksInLocation = Artwork.objects.filter(state=2).count()
    artistsTotal = Artist.objects.all().count()
    artistSpotlight = Artist.objects.filter(spotlight=True).first()
    artworksTimer = Artwork.objects.filter(timer__isnull=False).count()
    artworksBaclInLessThan = OrderArtworkRate.objects.filter(return_date__lte=make_aware(datetime.now() + timedelta(days=15)), return_date__gte=make_aware(datetime.now()))
    arrBackSoon = []
    for a in artworksBaclInLessThan:
        art = Artwork.objects.get(id=a.artwork_id)
        art.returnDate = a.return_date
        arrBackSoon.append(art)

    artworksmustBeBack = OrderArtworkRate.objects.filter(return_date__lte=make_aware(datetime.now()))
    arrMustBeBack = []
    for a in artworksmustBeBack:
        art = Artwork.objects.get(id=a.artwork_id)
        art.returnDate = a.return_date
        if art.state == 2:
            arrMustBeBack.append(art)
        
    
    return render(
        request, 
        'homepage/dashboard.html',
        {
            'orderWaiting': order,
            'totalArtworks': artworks,
            'artworksInLocation': artworksInLocation,
            'artistsTotal': artistsTotal,
            'artistSpotlight': artistSpotlight,
            'artworksTimer': artworksTimer,
            'artworksBackSoon': arrBackSoon,
            'artWorksMustBeBack': arrMustBeBack,
        }

    )

class SearchResultsView(ListView):
    model = Artwork
    template_name = 'search_results.html'
    def get_queryset(self):
        return Artwork.objects.filter(
            Q(name__icontains='el pueblo') | Q(artist__icontains='pablo')
        )

def search_result_view(request):    
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        artworks = Artwork.objects.filter(name__icontains=url_parameter)
    else:
        artworks = []

    ctx["artworks"] = artworks
    
    if request.is_ajax():
        html = render_to_string(
            template_name="artworks-results-partial.html", 
            context={"artworks": artworks}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "search_results.html", context=ctx)