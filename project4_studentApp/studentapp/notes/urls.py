from django.urls import path
from .views import upload_notes

urlpatterns = [
    path('', upload_notes, name='upload_notes'),
]