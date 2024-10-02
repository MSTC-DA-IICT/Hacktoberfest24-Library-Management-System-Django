from django.db import models

# Create your models here.
from django.db import models

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title

# Member Model
class Member(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# IssuedBook Model (connects Book and Member)
class IssuedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} issued to {self.member.name}'
