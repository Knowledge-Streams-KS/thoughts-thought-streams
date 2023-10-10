from django.urls import path
from . import views

urlpatterns = [

    path('ThoughtCreateView/', views.ThoughtCreateView.as_view(), name= 'ThoughtCreateView'),
    path('ThoughtListView/', views.ThoughtListView.as_view(), name= 'ThoughtListView'),
    path('ThoughtDetailView/<int:pk>', views.ThoughtDetailView.as_view(), name= 'ThoughtDetailView'),
    path('CommentCreateView/<int:thought_id>', views.CommentCreateView.as_view(), name= 'CommentCreateView'),
    path('ThoughtUpdateView/<int:pk>', views.ThoughtUpdateView.as_view(), name= 'ThoughtUpdateView'),
    path('share/<int:pk>/', views.share_thought, name='share-thought'),
    path('SharedWithMe/', views.SharedWithMe.as_view(), name='SharedWithMe'),





]
