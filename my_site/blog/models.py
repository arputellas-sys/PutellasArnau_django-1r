from django.db import models

class Author(models.Model):
    """
    Model que representa un autor del blog a la base de dades.
    """
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True) 
    bio = models.TextField()
    def total_posts(self):
        return self.post_set.count()

    def __str__(self):
        """
        Mètode que defineix com es mostrarà l'objecte (l'autor) al panell d'administració o a la consola.
        """
        return f"{self.name} {self.surname}" if self.surname else self.name

class Tag(models.Model):
    """
    Model que representa una etiqueta (categoria) per assignar als articles.
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Mostra el nom de l'etiqueta quan es crida l'objecte.
        """
        return self.name

class Post(models.Model):
    """
    Model principal que representa un article (post) publicat al blog.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300, blank=True) 
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        """
        Mostra el títol del post al panell d'administració per identificar-lo fàcilment.
        """
        return self.title