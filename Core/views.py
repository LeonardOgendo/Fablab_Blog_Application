from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post

# Create your views here.
 
def home(request):
    return render(request, 'home.html')
 
class PostsListView(ListView):
    model = Post
    template_name = 'all_posts.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'