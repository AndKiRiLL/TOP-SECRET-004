from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Category, Post
from .forms import FormCreate, FormEdit
from django.views.generic import ListView

def create(request):

    if request.method == "POST":
        post = Post()
        post.name = request.POST.get("name")
        post.caption = "---"
        post.img = request.POST.get("image")
        post.category_id = request.POST.get("category")
        post.author_id = request.POST.get("author")
        post.date = request.POST.get("date")
        post.save()
        return HttpResponseRedirect("/")

    categories = Category.objects.all()
    form_create = FormCreate
    return render(request, "app/Form_create.html", {"categories": categories, "form_create": form_create})

def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")

def edit(request, id):
    try:
        post = Post.objects.get(id=id)

        if request.method == "POST":
            post.name = request.POST.get("name")
            post.caption = "---"
            post.img = request.POST.get("img")
            post.category_id = request.POST.get("category")
            post.author_id = request.POST.get("author")
            post.date = request.POST.get("date")
            post.save()
            return HttpResponseRedirect("/")
        else:
            categories = Category.objects.all()
            form_edit = FormEdit(instance=post)
            return render(request, "app/edit.html", {"categories": categories, "form_edit": form_edit})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")

def index(request):
    initialize()
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request, "app/index.html", {"categories": categories, "posts": posts})

def initialize():
    if Category.objects.all().count() == 0:
        Category.objects.create(name="Политика")
        Category.objects.create(name="Экономика")
        Category.objects.create(name="Спорт")
        Category.objects.create(name="Кулинария")
        Category.objects.create(name="Природа")
        Category.objects.create(name="Строительство")


def news_political(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=2)
    return render(request, "app/index.html", {"categories": categories, "posts": posts})

def news_economic(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=3)
    return render(request, "app/index.html", {"categories": categories, "posts": posts})

def news_sport(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=4)
    return render(request, "app/index.html", {"categories": categories, "posts": posts})

def news_cooking(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=5)
    return render(request, "app/index.html", {"categories": categories, "posts": posts})

def news_nature(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=6)
    return render(request, "app/index.html", {"categories": categories, "posts": posts})

def news_construction(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=7)
    return render(request, "app/index.html", {"categories": categories, "posts": posts})
