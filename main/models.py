from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
LEVEL_CHOICES = [
        ("UNDERGRADUATE", "UNDERGRADUATE"),
        ("POSTGRADUATE", "POSTGRADUATE"),
        ("DEGREE APPRENTICESHIP", "DEGREE APPRENTICESHIP"),
        ("LEARNING AT WORK", "LEARNING AT WORK"),
        ("DISTANT LEARNING", "DISTANT LEARNING"),
        ("SHORT COURSES AND CPD", "SHORT COURSE AND CPD"),
    ]
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=100)
    uploaded_by = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    pdf = models.FileField(upload_to='bookapp/pdfs/')
    cover = models.ImageField(upload_to='bookapp\covers/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.message)

class Feedback(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.feedback
