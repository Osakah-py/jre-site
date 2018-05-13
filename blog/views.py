from django.shortcuts import render, get_object_or_404, render_to_response,redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.conf import settings
from .forms import PostForm

def post_list(request):
    titre="JRE - Collège de l'aigle"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'title':titre})	
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    titre= str(post.title)
    return render(request, 'blog/post_detail.html', {'post': post, 'title':titre})	
    print (titre+"a été ouvert dans le navigateur")

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def page_not_found_view(request):
     return render(request,'blog/404.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})