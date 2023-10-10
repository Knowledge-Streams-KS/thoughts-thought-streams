from django.db import models
from django.contrib.auth.models import AbstractUser



def image_handle(instance, img_name):
    return(f'images/profile/{img_name}')

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to=image_handle, blank=True, null=True)

    def __str__(self):
        return str(self.user.name) 