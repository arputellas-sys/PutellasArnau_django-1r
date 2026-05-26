from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

"""
Definició de les rutes (URLs) específiques de l'aplicació blog.
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts_list, name='posts-list'),
    
    # Agafa l'identificador (slug o id) de la URL i el passa com a variable a la vista
    path('posts/<slug:slug>', views.post_detail, name='posts-detail'),
    path('authors', views.authors_list, name='authors-list'),
    path('authors/<int:autor_id>', views.author_detail, name='author-detail'),
    path('tags', views.tags_list, name='tags-list'),
    path('tags/<str:tag>', views.tag_posts, name='tag-posts'),
]

# Permet carregar i mostrar imatges pujades durant l'execució en local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)