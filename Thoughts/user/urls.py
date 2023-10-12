from django.urls import path
from . import views

urlpatterns = [
    
    
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('ProfileCreateView/', views.ProfileCreateView.as_view(), name= 'ProfileCreateView'),
    # path('ProfileUpdateView/<int:pk>', views.ProfileUpdateView.as_view(), name= 'ProfileUpdateView'),
    path('user/profile/update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', views.ProfileDetail, name='ProfileDetail'),


    path('UserListView/', views.UserListView.as_view(), name= 'UserListView'),
    path('UserDetailView/<int:id>/', views.userDetail, name= 'UserDetailView'),


    
]
