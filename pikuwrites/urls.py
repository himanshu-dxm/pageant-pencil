
from django.urls import path
from . import views
from .views import PostDetailView
#from . import views

urlpatterns = [
    #path('',views.index,name="index"),
    path('',views.index,name="index"),
    path('article/<int:pk>',PostDetailView.as_view(),name="post-detail"),
    path('like/<int:pk>',views.poemlike,name="poem_like"),
    path('terms-and-conditions',views.terms,name="terms-and-conditions"),
    path('privacy-policy',views.privacyPolicy,name="privacy-policy"),
]
