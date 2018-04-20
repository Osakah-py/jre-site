from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
   list_display   = ('title', 'auteur', 'published_date')
   search_fields  = ('title', 'text')
   
admin.site.site_header = 'JRE - Administration'
admin.site.register(Post, PostAdmin)

