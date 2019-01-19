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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
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
    titre= "JRE - "+str(post.title)
    info = False
    warning = False      
    if request.method == "POST":
        if post.public == False :
            post.public = True
            post.save()
            info = True
        else:
            post.public = False
            post.save()
            warning = True      
    else :
        info = False
        warning = False 
    return render(request, 'blog/post_detail.html', {'post': post, 'title':titre, 'info':info, 'warning':warning})	

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def brouillons(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = posts.filter(public=False)
    return render(request, 'blog/brouillons.html', {'posts':posts})

def page_not_found_view(request):
     return render(request,'blog/404.html')

def post_new(request):
    titre= "JRE - Nouvel article"
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
    return render(request, 'blog/post_edit.html', {'form': form, 'title':titre})
	
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    titre= "JRE - "+str(post.title)+" - edition"
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'title':titre})
	
def gaspillage(request):
    titre="JRE - Groupe : gaspillage"
    groupe="Gaspillage"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    description = get_object_or_404(Descriptions, title="gaspillage")
    return render(request, 'blog/groupe.html', {'title':titre, 'description':description, 'posts': posts, 'groupe' : groupe})
	
def velo(request):
    groupe="vélo"
    titre="JRE - Groupe : "+groupe
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    description = get_object_or_404(Descriptions, title="vélo")
    return render(request, 'blog/groupe.html', {'title':titre, 'description':description, 'posts': posts, 'groupe' : groupe})
	
def armuresolaire(request):
    groupe="panneau solaire"
    titre="JRE - Groupe : "+groupe
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    description = get_object_or_404(Descriptions, title="armuresolaire")
    return render(request, 'blog/groupe.html', {'title':titre, 'description':description, 'posts': posts, 'groupe' : groupe})

def propos(request):
    titre="JRE - A propos"
    description = get_object_or_404(Descriptions, title="A propos")
    return render(request, 'blog/propos.html', {'title':titre, 'description':description})
	
def description_edit(request, pk):
    post = get_object_or_404(Descriptions, pk=pk)
    if request.method == "POST":
        form = DescriptionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(post.title)
    else:
        form = DescriptionForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
	
def color(request):
    titre= "JRE Documentation"
    return render(request, 'blog/color.html', {'title':titre})	