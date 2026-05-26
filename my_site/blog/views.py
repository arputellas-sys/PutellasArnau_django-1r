from django.shortcuts import get_object_or_404
from django.shortcuts import render
import datetime
from .models import Post, Author, Tag
from django.http import HttpResponse

def index(request):
    """
    Vista principal: mostra únicament els 3 últims posts publicats.
    """
    # Ordenem per data descendent i limitem els resultats als 3 primers
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})

def posts_list(request):
    """
    Vista que llista absolutament tots els posts del blog.
    """
    all_posts = Post.objects.order_by('-date')
    return render(request, 'blog/post_list.html', {'posts': all_posts})

def post_detail(request, slug):
    """
    Vista per llegir un article sencer a partir del seu identificador.
    """
    # Busca el post a la base de dades o retorna un error 404 si no existeix
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def authors_list(request):
    """
    Vista per llistar tots els autors registrats.
    """
    authors = Author.objects.all()
    return render(request, 'blog/authors_list.html', {'authors': authors})

def author_detail(request, autor_id):
    """
    Vista que mostra la informació d'un autor concret i filtra els articles que ha escrit.
    """
    author = get_object_or_404(Author, id=autor_id)
    # Filtrem la taula de posts perquè només mostrin els que pertanyen a aquest autor
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/author_detail.html', {'author': author, 'posts': posts})

def tags_list(request):
    """
    Vista per mostrar totes les etiquetes disponibles.
    """
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_posts(request, tag):
    """
    Vista que mostra tots els articles associats a una etiqueta específica.
    """
    tag_obj = get_object_or_404(Tag, name=tag)
    posts = Post.objects.filter(tags=tag_obj)
    return render(request, 'blog/tag_post.html', {'tag': tag_obj, 'posts': posts})


posts = [
    {
        'title': 'Primer post',
        'slug': 'primer-post',
        'content': 'Contingut del primer post.',
        'date': datetime.date(2024, 5, 1)
    },
    {
        'title': 'Segon post',
        'slug': 'segon-post',
        'content': 'Contingut del segon post.',
        'date': datetime.date(2024, 5, 5)
    },
    {
        'title': 'Tercer post',
        'slug': 'tercer-post',
        'content': 'Contingut del tercer post.',
        'date': datetime.date(2024, 5, 10)
    }
]