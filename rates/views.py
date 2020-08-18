import csv, io
from django.shortcuts import render, redirect
from .models import Rate
from .forms import RateForm, ModifyRateForm

# Create your views here.

def add(request):
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rates:rates_list")
    else:
        form = RateForm()
    return render(request, 'rates/add.html', {'form': form})

def update(request, rate_id):
    rate = Rate.objects.get(id=rate_id)      
    if request.method == 'POST':
        if 'delete_rate' in request.POST:
            rate.delete()                 
            return redirect("rates:rates_list")
        else:
            form = ModifyRateForm(request.POST, instance=rate)
            if form.is_valid():           
                form.save()
                return redirect("rates:rates_list")
    else:
        form = ModifyRateForm(instance=rate)
    return render(
        request,
        'rates/update.html',
        {
            'form': form,
        }
    ) 

def rates_list(request):
    rates = Rate.objects.all()    
    return render(request, 'rates/list_rates.html', {'rates': rates})

def rate_upload(request):
    template = "rates/import_rates.html"
    prompt = {
        'rate': 'Order of the csv should be , duration, rate'
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
        _, created = Rate.objects.update_or_create(
            duration=column[0],
            rate=column[1],
        )
    context = {}
    return render(request, template, context)