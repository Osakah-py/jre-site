from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^description/(?P<pk>[0-9]+)/$', views.description_edit, name='description_edit'),
	url(r'^documentation$', views.color, name='color'),
	url(r'^brouillons$', views.brouillons, name='draft'),
	url(r'^Gaspillage$', views.gaspillage, name='gaspillage'),
    url(r'^vélo$', views.velo, name='vélo'),
    url(r'^panneau solaire$', views.armuresolaire, name='panneau%20solaire'),
	url(r'^connexion$', views.authentification, name='authentification'),
	url(r'^a_propos$', views.propos, name='A propos'),
]