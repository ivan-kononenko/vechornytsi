from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'publication_date', 'pic')

admin.site.register(Post, PostAdmin)
