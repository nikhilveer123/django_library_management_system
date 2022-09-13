from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    return render(request,'home.html')



def operation(request):

    #data = Book.objects.all()  - retrives all the data from database

    ## Crud operation in Django
    # 1 create operation in django
    #temp = Book.objects.filter(edition=8.1)        -- filter the record from book library

    # GET  - return a single object . do not return new  querysets

    #temp = Book.objects.get(book_name='python')

    # CREATE OPERATION IN DJANGO  - a method for creating a object saving it all in one step
    '''
    data = Book(
        book_name = "ruby",author_name = "Yukihiro Matsumoto", published ="1995-06-14",edition=3.1

    )
    data.save()
    '''

    # second step to create a query set
    '''
    data = Book.objects.create(
        book_name = "ruby",author_name = "Yukihiro Matsumoto", published ="1995-06-14",edition=3.1

    )
    data.save(force_insert=True)
    '''

   # UPDATE OPERATION IN DJANGO

    #data = Book.objects.filter(edition = 9).update(book_name="Time is everyting")

    #data = Book.objects.all()

    # DELETE OPERATION IN DJANGO

    # DELETE A ONE RECORD
    '''
    data = Book.objects.get(edition=8.1)
    deleted_data = data.delete()   # deleted the data you can view admin side
    '''
    data = Book.objects.all()
    return render(request,'operation.html',{'data':data})
    