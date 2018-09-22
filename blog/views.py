from django.shortcuts import render, get_object_or_404, render_to_response,redirect
from django.utils import timezone
from .models import Post, Descriptions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.conf import settings
from .forms import PostForm, ConnexionForm, DescriptionForm

def post_list(request):
    titre="JRE - Collège de l'aigle"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'title':titre})	
	
def authentification(request):
    titre="JRE - Connexion"
    if request.method == "POST":
          form = ConnexionForm(request.POST)
          if form.is_valid():
               name = request.POST.get('username')
               password = request.POST.get('password')
               user = authenticate(username=name, password=password)  # Nous vérifions si les données sont correctes
               if user:  # Si l'objet renvoyé n'est pas None
                    login(request, user)  # nous connectons l'utilisateur
                    return redirect('post_list')
          else: # sinon une erreur sera affichée
               error = True
    else:
         form = ConnexionForm(request.POST)
    return render(request, 'blog/authentification.html', {'title':titre, 'form': form})	
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    titre= str(post.title)
    return render(request, 'blog/post_detail.html', {'post': post, 'title':titre})	

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
	
def gaspillage(request):
    titre="JRE - Groupe : gaspillage"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    description = get_object_or_404(Descriptions, title="gaspillage")
    return render(request, 'blog/gaspillage.html', {'title':titre, 'description':description, 'posts': posts})
	
def description_edit(request, pk):
    post = get_object_or_404(Descriptions, pk=pk)
    if request.method == "POST":
        form = DescriptionForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('gaspillage')
    else:
        form = DescriptionForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})