from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/abstravat.png')


    def __str__(self):
        return self.username
    

class Saved(models.Model):
    product = models.ForeignKey("products.Product",on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return "Saved by" + str(self.author.username)