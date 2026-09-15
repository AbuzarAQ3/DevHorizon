from django.shortcuts import render, get_object_or_404
from .models import Category, Blog
from django.http import HttpResponse

def blogRoot(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'blogs.html', context)

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id) # FUTURE use try catch or some logic for query failure -> redirects.
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)