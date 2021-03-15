from django.shortcuts import render
from .models import Post
from pip._vendor.requests.api import request
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.
#def index(request):
#   return HttpResponse('Hello')

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

