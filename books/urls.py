from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("books", views.books, name="books"),
    path("books/<int:id>", views.bookdetail, name="detail"),
    path("categories/<int:category_id>/books", views.books_by_category, name="books_by_category"),
    path("search/", views.search_results, name="search_results"),
]
