from django.shortcuts import render
from .forms import HomePageContentForm, ConceptContentForm
from .models import Content

def update_content(request):             
    content = Content.objects.last()  
    if request.method == 'POST':
        form = HomePageContentForm(request.POST, instance=content)
        formconcept = ConceptContentForm()
        if form.is_valid():           
            form.save()
    else:
        if content is None:
            form = HomePageContentForm()
            formconcept = ConceptContentForm()
        else:
            form = HomePageContentForm(instance=content)
            formconcept = ConceptContentForm(instance=content)
    return render(
        request,
        'content/update.html',
        {
            'form': form,
            'formconcept': formconcept,
        }
    ) 
