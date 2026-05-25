from django.test import TestCase
from django.db import IntegrityError
from blog.models import Tag

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Django")

    def test_tag_creation(self):
        """Comprova que el Tag es crea amb el nom correcte."""
        self.assertEqual(self.tag.name, "Django")

    def test_str_representation(self):
        """__str__ ha de retornar el nom del tag."""
        self.assertEqual(str(self.tag), "Django")

    def test_name_unique(self):
        """El camp name és únic: intentar crear-ne un de duplicat llança error."""
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="Django")
