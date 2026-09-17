from django.shortcuts import render, get_object_or_404
from .models import Category, Blog, Author
from django.http import HttpResponse
from django.db.models import Q

def homepage(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    try:
        author = Author.objects.get()
    # hard lesson, try does not work with all() or filter()
    except:
        author = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'author': author,
    }
    return render(request, 'homepage.html', context)

def blogs(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'blog':blog,
    }
    return render(request, 'blogs.html', context)

def blogs_search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'blogs_search.html', context)

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id) # FUTURE use try catch or some logic for query failure -> redirects.
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)

