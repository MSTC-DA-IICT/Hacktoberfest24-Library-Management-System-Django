from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    borrowed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    def borrow_book(self, user):
        if self.status == 'available':
            self.status = 'borrowed'
            self.borrowed_by = user
            self.save()
        else:
            raise ValidationError('This book is already borrowed.')

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            self.borrowed_by = None
            self.save()
        else:
            raise ValidationError('This book is not currently borrowed.')

    def __str__(self):
        return f"{self.status} : {self.title} by {self.author.name}"

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


# Genre Model
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# Borrower Model
class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name

