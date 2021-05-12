from django.shortcuts import render
from .models import Post,IpModel
from pip._vendor.requests.api import request
from django.views.generic import ListView,DetailView,CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#def index(request):
#   return HttpResponse('Hello')

def index(request):
    poems = Post.objects.all().filter(type="poem")
    quotes = Post.objects.all().filter(type="quote")
    mydict = {
        "poems" : poems.order_by('-updated_at'),
        "quotes" : quotes.order_by('-updated_at'),
        "object_list" : Post.objects.all().order_by('updated_at')
    }
    return render(request,'index.html',context=mydict)

def terms(request):
    return render(request,'terms-and-conditions.html')

def privacyPolicy(request):
    return render(request,'privacy.html')

# class IndexView(ListView):
#     model = Post
#     template_name = 'index.html'
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWADED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'poem.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        
        like_status = False
        ip = get_client_ip(request)
        if self.object.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
            like_status = True
        else:
            like_status = False
        
        context['like_status'] = like_status
        
        return self.render_to_response(context)

def poemlike(request,pk):
    post_id = request.POST.get('poem-id')
    post = Post.objects.get(pk=post_id)
    ip = get_client_ip(request)
    
    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    
    if post.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
        post.likes.remove(IpModel.objects.get(ip=ip))
    else :
        post.likes.add(IpModel.objects.get(ip=ip))
    
    return HttpResponseRedirect(reverse('post-detail' , args=[post_id]))