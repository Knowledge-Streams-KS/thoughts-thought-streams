from django.db import models
from user.models import User

# Create your models here.



def image_handle(instance, img_name):
    return(f'images/{instance.id}/{img_name}')



class Thought(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(User, related_name='shared_with')
    img = models.ImageField(upload_to=image_handle, blank=True, null=True)
    is_private = models.BooleanField(default=False)    

    def __str__(self):
        return self.title
    
    

class Comment(models.Model):
    text =  models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.text
