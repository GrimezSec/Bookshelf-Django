from django.shortcuts import render
from .models import Category, Book

# Create your views here.

def home(request):
    data = {
        "kategoriler" : Category.objects.all(),
        "kitaplar": Book.objects.filter(anasayfa=True)
    }
    return render(request, "index.html", data)

def books(request):
    data = {
        "kategoriler" : Category.objects.all(),
        "kitaplar": Book.objects.all()
    }
    return render(request, "books.html", data)

def bookdetail(request, id):
    data = {
        "kitap": Book.objects.get(id=id)
    }
    return render(request, "bookdetail.html", data)

def books_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    books_in_category = Book.objects.filter(category=category)
    data = {
        "kategoriler": Category.objects.all(),
        "kategori": category,
        "kitaplar": books_in_category
    }
    return render(request, "books_by_category.html", data)

def search_results(request):
    query = request.GET.get('q')
    kitaplar = Book.objects.filter(kitap_adi__icontains=query)
    data = {
        "kategoriler": Category.objects.all(),
        "kitaplar": kitaplar
    }
    return render(request, "search_results.html", data)