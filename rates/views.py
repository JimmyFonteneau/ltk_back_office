from django.shortcuts import render, redirect
from .models import Rate
from .forms import RateForm, ModifyRateForm

# Create your views here.

def add(request):
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rates/update/')
    else:
        form = RateForm()
    return render(request, 'rates/add.html', {'form': form})

def update(request):
    rates = Rate.objects.all()    
    forms = []
    index = 0
    if request.method == 'POST':
        for r in rates:
            index+=1
            form = ModifyRateForm(request.POST, instance=r, prefix="form"+str(index))
            if form.is_valid():
                form.save() 
            forms.append(ModifyRateForm(instance=r, prefix="form"+str(index)))
    else:            
        for r in rates:
            index+=1
            forms.append(ModifyRateForm(instance=r, prefix="form"+str(index)))
    return render(
        request,
        'rates/update.html',
        {
            'forms': forms,
        }
    )