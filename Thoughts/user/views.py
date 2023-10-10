from django.shortcuts import render,HttpResponse,redirect
from .models import User,Profile
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView 
from django.urls import reverse
from django.views.generic.list import ListView



# Create your views here.

def HomePage(request):
    return render (request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            error_message = "Your password and confirm password are not the same!!"

            # return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    else:
        error_message = ""

    return render (request,'signup.html' , {'error_message': error_message})



def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('ThoughtListView')
        else:
            return redirect('login')

    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('home')




class ProfileCreateView(CreateView):
    model = Profile
    fields = ['bio', 'address', 'img']

    def form_valid(self, form):
        user_profile, created = Profile.objects.get_or_create(user=self.request.user)

        if not created:
            user_profile.bio = form.cleaned_data['bio']
            user_profile.address = form.cleaned_data['address']
            user_profile.img = form.cleaned_data['img']
            user_profile.save()

        return redirect(reverse('ProfileDetail')) 
    


def ProfileDetail(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if created:
        return redirect(reverse('ProfileCreateView'))

    return render(request, 'Profile.html', {'user_profile': user_profile})



class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['bio', 'address', 'img']
    success_url = '/user/user/profile/'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)



class UserListView(ListView):
    model = User
    
    

