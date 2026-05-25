from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post

User = get_user_model()

class ViewsTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="joan", password="pwd123")
        self.post = Post.objects.create(
            title="Django Test",
            content="Contingut test",
            author=self.author
        )

    def test_list_view_status_code(self):
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertIn(self.post, response.context['posts'])

    def test_detail_view(self):
        url = reverse('post_detail', args=[self.post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
