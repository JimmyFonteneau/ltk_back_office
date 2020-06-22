from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView
from artworks.models import Artwork
from django.db.models import Q

def homepage(request):
    return render(
        request, 
        'homepage/homepage.html'
    )

class SearchResultsView(ListView):
    model = Artwork
    template_name = 'search_results.html'
    def get_queryset(self):
        return Artwork.objects.filter(
            Q(name__icontains='el pueblo') | Q(artist__icontains='pablo')
        )

def search_result_view(request):
    print('POPOPPOPOP')
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        artworks = Artwork.objects.filter(name__icontains=url_parameter)
    else:
        artworks = []

    ctx["artworks"] = artworks

    print('POPOPPOPOP')
    if request.is_ajax():
        html = render_to_string(
            template_name="homepage/artworks-results-partial.html", 
            context={"artworks": artworks}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "search_results.html", context=ctx)