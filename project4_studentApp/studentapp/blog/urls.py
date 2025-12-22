from django.urls import path
from .views import post_list, post_update, post_delete

urlpatterns = [
    path('', post_list, name='post_list'),
    path('update/<int:pk>/', post_update, name='post_update'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),
]