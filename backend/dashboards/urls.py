from django.urls import path, include
from . import views

urlpatterns = [
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # categories
    path('dashboard/categories/', views.categories, name='categories'),
    path('dashboard/categories/add/', views.add_category, name='add_category'),
    path('dashboard/categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('dashboard/categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    # posts
    path('dashboard/posts/', views.posts, name='posts'),
    path('dashboard/posts/add/', views.add_post, name='add_post'),
    path('dashboard/posts/edit/<int:pk>', views.edit_post, name='edit_post'),
    path('dashboard/posts/delete/<int:pk>/', views.delete_post, name='delete_post'),

]