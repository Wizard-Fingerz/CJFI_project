from django.contrib import admin
from .models import Book, Chat, Feedback

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author","publisher", "pdf")
admin.site.register(Book, BookAdmin)
admin.site.register([Chat, Feedback])