from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})