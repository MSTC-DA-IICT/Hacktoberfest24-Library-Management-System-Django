"""
URL configuration for LibraryManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LibraryManagementSystem import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),  # List all books
    path('book/<int:pk>/', views.book_detail, name='book_detail'),  # Book detail view
    path('book/new/', views.book_create, name='book_create'),  # Create a new book
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),  # Edit an existing book
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),  # Delete a book
]

