import uuid
from django.db import models

# Create your models here.

class Book(models.Model): 
    book_name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30,default='abcd')
    published = models.DateField()
    edition = models.CharField(max_length=20)

    def __str__(self):
       return self.book_name    

