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