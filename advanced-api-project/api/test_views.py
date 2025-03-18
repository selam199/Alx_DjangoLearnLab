from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):
    
    def setUp(self):
        """Set up test data for the Book API"""
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create test books
        self.book1 = Book.objects.create(title="Django Unchained", author="Quentin Tarantino", publication_year=2012)
        self.book2 = Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2016)

        # Define URLs
        self.list_url = reverse('book-list')  # Assumes you're using DRF viewsets with named routes
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})  # For individual book details

    def authenticate(self):
        """Authenticate test user"""
        self.client.login(username='testuser', password='testpassword')
        
        def test_get_books_list(self):
            """Test retrieving a list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure two books exist
        
        def test_get_single_book(self):
            """Test retrieving details of a single book"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
    
    
        def test_create_book(self):
            """Test adding a new book"""
        self.authenticate()
        data = {'title': 'New Django Book', 'author': 'John Doe', 'publication_year': 2023}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # Ensure book count increased
         
         
        def test_update_book(self):
            """Test modifying an existing book"""
        self.authenticate()
        data = {'title': 'Updated Title', 'author': 'Updated Author', 'publication_year': 2025}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')
        
        def test_delete_book(self):
            """Test removing a book"""
        self.authenticate()
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
        
        def test_filter_books_by_title(self):
            """Test filtering books by title"""
        response = self.client.get(f"{self.list_url}?title=Django Unchained")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        
        def test_search_books_by_author(self):
            """Test searching books by author"""
        response = self.client.get(f"{self.list_url}?search=Eric Matthes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        def test_order_books_by_publication_year(self):
            """Test ordering books by publication year"""
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['publication_year'] <= response.data[1]['publication_year'])






