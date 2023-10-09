from django.urls import path
from . import views

urlpatterns = [

    path('ThoughtCreateView/', views.ThoughtCreateView.as_view(), name= 'ThoughtCreateView'),
    path('ThoughtListView/', views.ThoughtListView.as_view(), name= 'ThoughtListView'),
    
]
