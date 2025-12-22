from django.shortcuts import render, redirect
from .models import NoteImage
from .forms import NoteImageForm

def upload_notes(request):
    images = NoteImage.objects.all()
    form = NoteImageForm()

    if request.method == 'POST':
        form = NoteImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_notes')

    return render(request, 'notes/upload_notes.html', {
        'images': images,
        'form': form
    })