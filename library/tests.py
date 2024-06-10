from django.test import TestCase
from .models import Author

class AuthorModelTest(TestCase):
    def setUp(self):
        Author.objects.create(first_name="John", last_name="Doe", birth_date="1980-01-01")

    def test_author_str(self):
        author = Author.objects.get(id=1)
        self.assertEqual(str(author), "John Doe")
