from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="James")
        self.author2 = Author.objects.create(name="Joseph")

        # Create books linked to authors
        self.book1 = Book.objects.create(title='Help of the Nation', publication_year=2014, author=self.author1)
        self.book2 = Book.objects.create(title='Schools of Anger', publication_year=2013, author=self.author2)

        # Set up endpoints
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    # Fetch all books
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Fetch a specific book
    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Help of the Nation')

    # Ensure unauthenticated users cannot create books
    def test_create_book_unauthenticated(self):
        data = {'title': 'New Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Authenticated user can create books
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='pass123')
        data = {'title': 'New Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # Authenticated user can update books
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='pass123')
        data = {'title': 'Updated Title', 'publication_year': 2014, 'author': self.author1.id}
        response = self.client.put(self.update_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    # Authenticated user can delete books
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # Filters books by publication_year
    def test_filter_books_by_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2014")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Help of the Nation')

    # Searches books by title keyword
    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=Anger")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Schools of Anger')

    # Orders books by title descending
    def test_order_books_by_title_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Schools of Anger')

    # Validates that future publication years are invalid
    def test_create_book_with_future_year(self):
        self.client.login(username='testuser', password='pass123')
        future_year = 3000
        data = {'title': 'Future Book', 'publication_year': future_year, 'author': self.author1.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
