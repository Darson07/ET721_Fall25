from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
# List view
def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Detail view
def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create view
def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()

    return render(request, 'blog/post_form.html', {'form': form})

# Update view
def post_edit(request, id):
    post = get_object_or_404(BlogPost, id=id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})