from django.contrib import admin
from .models import Post, Categorie, Descriptions

class PostAdmin(admin.ModelAdmin):
   list_display   = ('title', 'auteur', 'published_date')
   search_fields  = ('title', 'text')

class CategorieAdmin(admin.ModelAdmin):
   list_display   = ('nom',)
   search_fields  = ('nom',)
   
admin.site.site_header = 'JRE - Administration'
admin.site.register(Post, PostAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Descriptions)
