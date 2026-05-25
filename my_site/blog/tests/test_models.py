from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, Tag

User = get_user_model()

class ModelsTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="ana", password="pwd123")
        self.tag1 = Tag.objects.create(name="django")
        self.tag2 = Tag.objects.create(name="testing")

        self.post = Post.objects.create(
            title="Hola món",
            content="Contingut de prova",
            author=self.author
        )
        # ManyToMany
        self.post.tags.set([self.tag1, self.tag2])

    def test_author_relation(self):
        self.assertEqual(self.post.author.username, "ana")

    def test_tags_relation(self):
        tags = list(self.post.tags.all())
        self.assertIn(self.tag1, tags)
        self.assertIn(self.tag2, tags)

    def test_str_methods(self):
        self.assertEqual(str(self.post), "Hola món")
        self.assertEqual(str(self.tag1), "django")
