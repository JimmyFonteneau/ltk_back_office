from django.shortcuts import render, redirect
from .models import Configuration
from .forms import ModifyConfiguration

def update(request):
    rate = Configuration.objects.all().first()     
    if request.method == 'POST':     
        if rate is None:
            form = ModifyConfiguration(request.POST)
        else:     
            form = ModifyConfiguration(request.POST, instance=rate)        
        if form.is_valid():           
            form.save()
            return redirect("dashboard")
    else:
        if rate is None:
            form = ModifyConfiguration()
        else:     
            form = ModifyConfiguration(instance=rate)
    return render(
        request,
        'configuration/update.html',
        {
            'form': form,
        }
    )
