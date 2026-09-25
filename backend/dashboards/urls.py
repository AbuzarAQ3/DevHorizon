from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/categories', views.categories, name='categories'),
    path('dashboard/categories/add/', views.add_category, name='add_category'),
    path('dashboard/categories/edit/<int:pk>', views.edit_category, name='edit_category'),
    path('dashboard/categories/delete/<int:pk>', views.delete_category, name='delete_category'),


]