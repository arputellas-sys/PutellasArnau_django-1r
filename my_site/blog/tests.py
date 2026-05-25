from django.test import TestCase
from .models import Tag

class TagModelTest(TestCase):
    def setUp(self):
        Tag.objects.create(name='prova')

    def test_tag_str(self):
        tag = Tag.objects.get(name='prova')
        self.assertEqual(str(tag), 'prova')
