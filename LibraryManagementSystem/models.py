from django.db import models
from django.contrib.auth.models import User

models_branch

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

