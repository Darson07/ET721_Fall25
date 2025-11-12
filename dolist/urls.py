from django.urls import path
from . import views

urlpatterns = [
    # load page of the app will be sent to the index.html
    path('', views.index, name = 'index'),
]