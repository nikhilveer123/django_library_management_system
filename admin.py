from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    data = [
        'id','book_name','author_name','published','edition'
    ]

 

