from django.shortcuts import render, get_object_or_404, render_to_response,redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

class LoginView(TemplateView):

  template_name = 'blog/post_list.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)

class LogoutView(TemplateView):

  template_name = 'blog/post_list.html'

  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)
	
def post_list(request):
    titre="JRE - Collège de l'aigle"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'title':titre})	
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    titre= str(post.title)
    return render(request, 'blog/post_detail.html', {'post': post, 'title':titre})	
    print (titre+"a été ouvert dans le navigateur")

