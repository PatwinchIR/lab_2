from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book, Author

add=[False,False]
def index(request):
    book_list=Book.objects.all()
    author_list=Author.objects.all()
    context={'book_list':book_list,'author_list':author_list}
    if request.method == 'POST':
        search_name = request.POST.get('author_name','')
        try:
            author = Author.objects.get(Name=search_name)
            book_list_of_author = Book.objects.filter(AuthorID=author.AuthorID)
            context = {'book_list': book_list,'author_lib':book_list_of_author,'author_name':author.Name,'author_list':author_list}
        except:
            book_list_of_author = ['empty']
            context = {'book_list': book_list,'author_empty':book_list_of_author,'author_name':search_name,'author_list':author_list}
    if add[0]:
        if add[1]:
            context['bad_parameters']=['not_empty']
            add[0]=False
            add[1]=False
        else:
            add[0]=False
            add[1]=False
            pass
    else:
        add[0]=False
        add[1]=False
        pass
    return render(request,'libman/index.html',context)

update_book_list=[]
def edit(request):
    if request.method=='GET':
        pass
        book=Book.objects.get(ISBN=request.GET.get('update_book_ISBN'))
        update_book_list.append(book)
        author_list=Author.objects.all()
        context={'book':book,'author_list':author_list}
        return render(request,'libman/edit.html',context)
    else:
        try:
            book=update_book_list[-1]
            author=Author.objects.get(AuthorID=request.POST.get('update_book_authorid'))
            book.AuthorID = author
            book.Publisher = request.POST.get('update_book_publisher')
            book.PublishDate = request.POST.get('update_book_publishdate')
            book.Price = request.POST.get('update_book_price')
            book.save()
            return HttpResponseRedirect('/')
        except:
            return render(request,'libman/edit.html',{'bad_parameters':['not_empty']})

def details(request, bookisbn):
    book=Book.objects.get(ISBN=bookisbn)
    author=Author.objects.get(AuthorID=book.AuthorID)
    context={'book':book,'author':author}
    return render(request,'libman/details.html',context)

def delete(request):
    try:
        Book.objects.get(ISBN=request.GET.get('delete_book_ISBN')).delete()
    except:
        pass
    return HttpResponseRedirect('/')

def add_book(request):
    add[0]=True
    get=request.GET
    try:
        new_book=Book(
            ISBN=get['add_book_isbn'],
            Title=get['add_book_title'],
            AuthorID=Author.objects.get(AuthorID=get['add_book_authorid']),
            Publisher=get['add_book_publisher'],
            PublishDate=get['add_book_publishdate'],
            Price=get['add_book_price']
        )
        new_book.save()
        add[1]=False
        return HttpResponseRedirect('/')
    except:
        add[1]=True
        return HttpResponseRedirect('/')

def add_author(request):
    if request.method=='GET':
        return render(request,'libman/add_author.html',{})
    else:
        post=request.POST
        try:
            new_author=Author(
                AuthorID=post['AuthorID'],
                Name=post['Name'],
                Age=post['Age'],
                Country=post['Country']
            )
            new_author.save()
            return HttpResponseRedirect('/')
        except:
            return render(request,'libman/add_author.html',{'bad_parameters':['not_empty']})
        

