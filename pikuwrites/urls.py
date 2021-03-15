
from django.urls import path
from .views import IndexView,PostDetailView
#from . import views

urlpatterns = [
    #path('',views.index,name="index"),
    path('',IndexView.as_view(),name="index"),
    path('article/<int:pk>',PostDetailView.as_view(),name="post-detail"),
]
