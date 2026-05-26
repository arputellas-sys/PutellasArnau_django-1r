from django.contrib import admin
from blog.models import Post, Author, Tag

"""
Enregistrem els models perquè es puguin gestionar des del panell /admin.
"""
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)