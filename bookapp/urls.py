from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:id>/", views.book_detail, name="book_detail"),
    path("create/", views.create_book, name="create_book"),
    path("<int:id>/update/", views.update_book, name="update_book"),
    path("<int:id>/delete/", views.delete_book, name="delete_book"),
]