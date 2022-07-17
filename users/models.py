from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image
# Create your models here.



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to ='profile_pics')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

