from django.db import models
import django_filters

# Create your models here.
LEVEL_CHOICES = [
        ("UNDERGRADUATE", "UNDERGRADUATE"),
        ("POSTGRADUATE", "POSTGRADUATE"),
        ("DEGREE APPRENTICESHIP", "DEGREE APPRENTICESHIP"),
        ("LEARNING AT WORK", "LEARNING AT WORK"),
        ("DISTANT LEARNING", "DISTANT LEARNING"),
        ("SHORT COURSES AND CPD", "SHORT COURSE AND CPD"),
    ]
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
    


