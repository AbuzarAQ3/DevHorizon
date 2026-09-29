from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from . import forms
from .forms import CategoryForm, PostForm

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard.html', context)

def categories(request):
    return render(request, 'categories.html')

def add_category(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = forms.CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.author
            post.save()
            post.slug = slugify(form.cleaned_data['title']) + '-' + str(post.id)
            # future update, to transfer slug generations inside models as it is the prod standard
            post.save()
            return redirect('posts')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' +str(post.id)
            post.save()
            return redirect('posts')
    form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')