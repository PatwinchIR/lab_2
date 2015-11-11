from django.contrib import admin
from libman.models import Book, Author
class bookadmin(admin.ModelAdmin):
    fields = ('ISBN','Title','AuthorID','Publisher','PublishDate','Price')

class authoradmin(admin.ModelAdmin):
    fields = ('AuthorID','Name','Age','Country')

admin.site.register(Author, authoradmin)
admin.site.register(Book, bookadmin)