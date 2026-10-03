from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Category, Blog, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def homepage(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    try:
        author = User.objects.get()
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
    post = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.post = post
        comment.comment_body = request.POST['comment_body']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    comments_count = comments.count()
    context = {
        'blog':post,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'blogs.html', context)

def blogs_search(request):
    keyword = request.GET.get('keyword', '')
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

