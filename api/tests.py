<<<<<<< HEAD
# api/tests.py
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class AuthorTestCase(APITestCase):
    def setUp(self):
        # Create some authors and books
        self.author1 = Author.objects.create(name="James")
        self.book1 = Book.objects.create(
            title="May of the Year",
            publication_year=2014,
            author=self.author1
        )

        self.author2 = Author.objects.create(name="Joseph")
        self.book2 = Book.objects.create(
            title="Lead of Vamhu",
            publication_year=2020,
            author=self.author2
        )

    def test_authors_exist(self):
        # Test if authors were created successfully
        authors_count = Author.objects.count()
        self.assertEqual(authors_count, 2)

    def test_books_exist(self):
        # Test if books were created successfully
        books_count = Book.objects.count()
        self.assertEqual(books_count, 2)

    def test_author_books_relationship(self):
        # Test if the books are linked to the correct author
        self.assertEqual(self.author1.book_set.first().title, "May of the Year")
        self.assertEqual(self.author2.book_set.first().title, "Lead of Vamhu")
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> c94f0dd118e55d659f3cdd132b0de343570dbc87
