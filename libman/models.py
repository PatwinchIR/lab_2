from django.db import models
class Book(models.Model):
    ISBN=models.CharField(max_length=100,primary_key=True)
    Title=models.CharField(max_length=100)
    AuthorID=models.ForeignKey('Author')
    Publisher=models.CharField(max_length=100)
    PublishDate=models.DateField()
    Price=models.FloatField()
    def __str__(self):
        return self.ISBN

class Author(models.Model):
    AuthorID=models.CharField(max_length=50,primary_key=True)
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Country=models.CharField(max_length=50)
    def __str__(self):
        return self.AuthorID


