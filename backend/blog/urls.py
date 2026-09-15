from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogRoot, name='blogRoot'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]
