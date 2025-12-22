from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Existing list & create view
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'form': form
    })

# Update view
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    return render(request, 'blog/post_form.html', {
        'form': form,
        'post': post
    })

# Delete view
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {
        'post': post
    })