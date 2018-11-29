from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('labs', views.lab_list, name='lab_list'),
    path('lab/<int:pk>/', views.lab_detail, name='lab_detail'),
    path('lab/new', views.lab_new, name='lab_new'),
    path('lab/<int:pk>/edit', views.lab_edit, name='lab_edit'),
    path('lab/<int:pk>/remove', views.lab_remove, name='lab_remove'),

    path('lab/<int:pk>/part', views.add_part_to_lab, name="add_part_to_lab"),

    path('groups', views.group_list, name='group_list'),
    path('group/<int:pk>/', views.group_detail, name='group_detail'),
    path('group/new', views.group_new, name='group_new'),
    path('group/<int:pk>/edit', views.group_edit, name='group_edit'),
    path('group/<int:pk>/remove', views.group_remove, name='group_remove'),

    path('help_queue', views.help_queue, name='help_queue'),
    path('help_list', views.help_list, name='help_list'),
    path('help/<int:pk>/help_edit', views.help_edit, name='help_edit'),

    path('status_list', views.status_list, name='status_list'),
]
