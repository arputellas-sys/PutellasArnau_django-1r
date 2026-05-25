from django.shortcuts import get_object_or_404
from django.shortcuts import render
import datetime
from .models import Post, Author, Tag
from .models import Author

# Create your views here.
from django.http import HttpResponse

def index(request):
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts_list(request):
    all_posts = Post.objects.order_by('-date')
    return render(request, 'blog/post_list.html', {'posts': all_posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors_list.html', {'authors': authors})

def author_detail(request, autor_id):
    author = get_object_or_404(Author, id=autor_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/author_detail.html', {'author': author, 'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_posts(request, tag):
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

