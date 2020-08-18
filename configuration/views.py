from django.shortcuts import render, redirect
from .models import Configuration
from .forms import ModifyConfiguration

def update(request):
    configuration = Configuration.objects.all().first()     
    if request.method == 'POST':     
        if configuration is None:
            form = ModifyConfiguration(request.POST)
        else:     
            form = ModifyConfiguration(request.POST, instance=configuration)        
        if form.is_valid():           
            form.save()
            return redirect("dashboard")
    else:
        if configuration is None:
            form = ModifyConfiguration()
        else:     
            form = ModifyConfiguration(instance=configuration)
    return render(
        request,
        'configuration/update.html',
        {
            'form': form,
        }
    )
