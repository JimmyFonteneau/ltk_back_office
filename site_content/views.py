from django.shortcuts import render
from .forms import HomePageContentForm, ConceptContentForm, AllContent
from .models import Content

def update_content(request):             
    content = Content.objects.last()  
    if request.method == 'POST':
        form = AllContent(request.POST, instance=content)      
        if form.is_valid():           
            form.save()
    else:
        if content is None:
            form = AllContent()
        else:
            form = AllContent(instance=content)
    return render(
        request,
        'content/update.html',
        {
            'form': form,
        }
    ) 
