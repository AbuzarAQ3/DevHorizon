from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blogs/<slug:slug>/', views.blogs, name='blogs'),
    path('blogs/search/', views.blogs_search, name='blogs_search'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]
