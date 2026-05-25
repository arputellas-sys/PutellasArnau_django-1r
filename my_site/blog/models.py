from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True) 
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}" if self.surname else self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300, blank=True) 
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title