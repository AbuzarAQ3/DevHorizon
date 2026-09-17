from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ('Published', 'Publish')
)
    
class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    author_about = models.CharField(max_length=100, blank=True)
    author_description = models.TextField(max_length=250, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name.username
    
    class Meta:
        verbose_name_plural = 'Authors'
        
class Socialaccounts(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.platform
    
    class Meta:
        verbose_name_plural = 'Socialaccounts'
        
class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=250)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(choices=STATUS_CHOICES, default='Draft', max_length=10)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    