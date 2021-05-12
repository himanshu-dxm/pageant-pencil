
from django.urls import path , re_path 
from . import views
from .views import PostDetailView
#from . import views

urlpatterns = [
    #path('',views.index,name="index"),
    path('',views.index,name="index"),
    path('article/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    # re_path(r'^article/(?P<pk>[0-9]{2})/$',PostDetailView.as_view(),name="post-detail"),
    path('like/<int:pk>/',views.poemlike,name="poem_like"),
    path('terms-and-conditions/',views.terms,name="terms-and-conditions"),
    path('privacy-policy/',views.privacyPolicy,name="privacy-policy"),
]
