from django.test import TestCase
from django.urls import reverse, resolve
from dolist.views import index, addTodoItem, completedTodo
from dolist.models import Todolist

class TestUrls(TestCase):
    def test_index_url(self):
        # Test that the index URL resolves to the correct view.
        url = reverse('index')

        # Ensure the URL is correctly mapped to the index view
        self.assertEqual(resolve(url).func, index)

    def test_add_url(self):
        # Test that the add URL resolves to the correct view.
        url = reverse('add')

        # Ensure the URL is correctly mapped to the addTodoItem view
        self.assertEqual(resolve(url).func, addTodoItem)

    def test_completed_url(self):
        # Test that the completed URL resolves to the correct view.
        url = reverse('completed', args=[1]) # Example todo_id = 1

        # Ensure the URL is correctly mapped to the completedTodo view
        self.assertEqual(resolve(url).func, completedTodo)

    def test_urls_status_codes(self):
        # Test that the URLs return the correct status codes.
        # Test the index URL
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        # Test the add URL (should be accessible via POST)
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 405) # Method Not Allowed (GET not allowed)

        # Test the completed URL with a valid todo_id (should redirect)
        response = self.client.get(reverse('completed', args=[1])) # Assuming 1 is a valid todo_id
        self.assertEqual(response.status_code, 302) # Redirect to index after completing task