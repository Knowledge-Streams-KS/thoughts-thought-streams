from django.shortcuts import render,HttpResponse,redirect
from .models import User,Profile
from thought.models import Thought
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView 
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



# Create your views here.

# VIEW FOR HOMEPAGE
def HomePage(request):
    return render (request,'home.html')


# VIEW FOR SIGNUP PAGE
def SignupPage(request):
    try:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')

            if not email or not uname or not pass1:
                error_message = "All fields required"
                return render (request,'signup.html' , {'error_message': error_message})

                
            user = User.objects.filter(username=uname)
            email = User.objects.filter(email=email)            


            if user:
                error_message = "Username already exists"
                return render (request,'signup.html' , {'error_message': error_message})

            elif email:
                error_message = "Email already exists"
                print(email)
                return render (request,'signup.html' , {'error_message': error_message})
                
            elif pass1!=pass2:
                error_message = "Password do not match!!"
                return render (request,'signup.html' , {'error_message': error_message})
            
            elif len(pass1)<=8:
                error_message = "Password must be 8 character atleast!!"
                return render (request,'signup.html' , {'error_message': error_message})

            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')    

        return render (request,'signup.html')
    
    except:
        error_message = "All fields required"
        return render (request,'signup.html' , {'error_message': error_message})



# VIEW FOR LOGINPAGE
def LoginPage(request): 
    try:   
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request,username=username,password=pass1)
            
            if user is not None:
                login(request,user)
                return redirect('ThoughtListView')
            else:
                error_message = "Username or password do not match"
                return render (request,'login.html' , {'error_message': error_message})
                
        return render (request,'login.html')
    
    except:
        error_message = "All fields required"
        return render (request,'signup.html' , {'error_message': error_message})



# VIEW FOR LOGOUT
def LogoutPage(request):
    logout(request)
    return redirect('home')



# VIEW FOR CREATE USER PROFILE
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
    

# VIEW fOR PROFILE DETAILS
def ProfileDetail(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    
    if created:
        return redirect(reverse('ProfileCreateView'))

    return render(request, 'profile.html', {'user_profile': user_profile})



# VIEW FOR PROFILE UPDATE
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['bio', 'address', 'img']
    success_url = '/user/profile/'

    def get_object(self):
        return Profile.objects.get(user=self.request.user)



# VIEW FOR USER LIST
class UserListView(ListView):
    model = User
    
    
    
# VIEW FOR USER DETAILS    
def userDetail(request, id):
    detail = Thought.objects.filter(author__id=id)
    author = User.objects.get(id=id)
    
    return render(request, 'user_detail.html' , {'detail':detail, 'author':author} )
