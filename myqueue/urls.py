from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_list, name='lab_list'),
    path('lab/<int:pk>/', views.lab_detail, name='lab_detail'),
    path('lab/new', views.lab_new, name='lab_new'),
    path('lab/<int:pk>/edit', views.lab_edit, name='lab_edit'),
]