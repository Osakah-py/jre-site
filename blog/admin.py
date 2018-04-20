from django.contrib import admin
from .models import Post

admin.site.site_header = 'JRE - Administration'

admin.site.register(Post)