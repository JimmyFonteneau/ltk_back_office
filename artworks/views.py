import csv, io
from django.shortcuts import render, redirect
from .forms import ArtworkForm, ModifyArtworkForm, StyleForm, CategoryForm, StoragePlaceForm
from .models import Artwork, Artwork_Style, Artwork_Category, Artwork_Storage_Place
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from carts.forms import CartAddArtworkForm
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
import copy

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
        if 'delete_artwork' in request.POST:
            artwork.delete()                     
            return redirect("artworks:artworks_list")
        elif 'duplicate_artwork' in request.POST:            
            a = Artwork(state= 1, name=artwork.name, height= artwork.height, width= artwork.width, artist= artwork.artist, photo= artwork.photo, price= artwork.price, style= artwork.style, category= artwork.category, storage_place= artwork.storage_place)
            a.save()
            return redirect("artworks:artworks_list")
        else:
            form = ModifyArtworkForm(request.POST, request.FILES, instance=artwork)
            if form.is_valid():           
                form.save()
                return redirect("artworks:artworks_list")
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
    categories = Artwork_Category.objects.all()
    storage_places = Artwork_Storage_Place.objects.all()

    ctx = {}
    style = request.GET.get("s")
    category = request.GET.get("c")
    sp = request.GET.get("sp")
    st = request.GET.get("st")

    if style:       
        if int(style) > 0:
            artworks = artworks.filter(style=style)
    
    if category:       
        if int(category) > 0:
            artworks = artworks.filter(category=category)
    
    if sp:       
        if int(sp) > 0:
            artworks = artworks.filter(storage_place=sp)
    
    if st:       
        if int(st) > 0:
            artworks = artworks.filter(state=st)
    
    ctx["artworks"] = artworks

    if request.user.is_superuser:
        if request.is_ajax():
            html = render_to_string(
                template_name="artworks/artworks_filtered_admin.html", 
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
                'categories': categories,
                'storage_places': storage_places,
                'states': Artwork.ARTWORK_STATES,
            }
        )
    else :
        paginator = Paginator(artworks, 8)
        page = request.GET.get('page')
        artworks = paginator.get_page(page)
        if request.is_ajax():
            html = render_to_string(
                template_name="artworks/artworks_filtered.html", 
                context={"artworks": artworks}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)
        return render(
            request, 
            'artworks/artworks_list.html', 
            {
                'artworks': artworks,
                'styles': styles,
                'categories': categories,
            }
        )

def artwork(request, artwork_id):             
    artwork = Artwork.objects.get(id=artwork_id)
    cart_artwork_form = CartAddArtworkForm()
    artworksWithSameStyle = Artwork.objects.filter(style_id=artwork.style_id)[:4] 
    return render(
        request,
        'artworks/artwork.html',
        {
            'artwork': artwork,
            'cart_artwork_form': cart_artwork_form,
            'artworksWithSameStyle': artworksWithSameStyle,
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

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect("artworks:artworks_list")
    else:
        form = CategoryForm()
    return render(request, 'artworks/add_category.html', {'form': form})

def add_storage_place(request):
    if request.method == "POST":
        form = StoragePlaceForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect("artworks:artworks_list")
    else:
        form = StoragePlaceForm()
    return render(request, 'artworks/add_storage_place.html', {'form': form})

def all_style(request):
    styles = Artwork_Style.objects.all()    
    return render(request, 'artworks/list_style.html', {'styles': styles})

def update_style(request, style_id):             
    style = Artwork_Style.objects.get(id=style_id)    
    if request.method == 'POST':
        if 'delete_style' in request.POST:
            style.delete()                 
            return redirect("artworks:all_style")
        else:
            form = StyleForm(request.POST, instance=style)
            if form.is_valid():           
                form.save()
                return redirect("artworks:all_style")
    else:
        form = StyleForm(instance=style)
    return render(
        request,
        'artworks/style_update.html',
        {
            'form': form,
        }
    ) 

def all_category(request):
    categories = Artwork_Category.objects.all()    
    return render(request, 'artworks/list_category.html', {'categories': categories})

def update_category(request, category_id):             
    category = Artwork_Category.objects.get(id=category_id)    
    if request.method == 'POST':
        if 'delete_category' in request.POST:
            category.delete()                 
            return redirect("artworks:all_category")
        else:
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():           
                form.save()
                return redirect("artworks:all_category")
    else:
        form = CategoryForm(instance=category)
    return render(
        request,
        'artworks/category_update.html',
        {
            'form': form,
        }
    ) 

def all_storage_place(request):
    storage_places = Artwork_Storage_Place.objects.all()    
    return render(request, 'artworks/list_storage_place.html', {'storage_places': storage_places})

def update_storage_place(request, storage_place_id):             
    storage_place = Artwork_Storage_Place.objects.get(id=storage_place_id)    
    if request.method == 'POST':
        if 'delete_storage_place' in request.POST:
            storage_place.delete()                 
            return redirect("artworks:all_storage_place")
        else:
            form = StoragePlaceForm(request.POST, instance=storage_place)
            if form.is_valid():           
                form.save()
                return redirect("artworks:all_storage_place")
    else:
        form = StoragePlaceForm(instance=storage_place)
    return render(
        request,
        'artworks/storage_place_update.html',
        {
            'form': form,
        }
    ) 

def artwork_upload(request):
    template = "artworks/import_artworks.html"
    prompt = {
        'artwork': 'Order of the csv should be , name, height, width, price, description, introduction'
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
        _, created = Artwork.objects.update_or_create(
            name=column[0],
            height=column[1],
            width=column[2],
            price=column[3],
            description=column[4],
            introduction=column[5],
        )
    context = {}
    return render(request, template, context)
