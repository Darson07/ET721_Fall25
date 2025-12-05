from django.test import TestCase
from django.urls import reverse
from dolist.models import Todolist
from dolist.forms import TodoListForm
from dolist.views import addTodoItem, completedTodo, deletecompleted, deleteAll

class TodoViewsTestCase(TestCase):
    def setUp(self):
        # Create initial data for testing
        self.task1 = Todolist.objects.create(text="Task 1", completed=False)
        self.task2 = Todolist.objects.create(text="Task 2", completed=False)
        self.task3 = Todolist.objects.create(text="Task 3", completed=True)
    
    def test_index_view(self):
        # Test the index view renders the correct context and template.
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # Check if all tasks are included in the context
        self.assertQuerySetEqual(
            response.context['todo_tasks'],
            Todolist.objects.order_by('id'),
            transform=lambda x: x,
        )
        self.assertIsInstance(response.context['form'], TodoListForm)

    def test_add_todo_item_view_valid_data(self):
        # Test adding a valid todo item.
        response = self.client.post(reverse(addTodoItem), {'text':'Task 3'})
        self.assertEqual(response.status_code,302)# Should redirect to 'index'

        # Verify the new task was added
        self.assertEqual(Todolist.objects.count(), 3)
        self.assertTrue(Todolist.objects.filter(text='Task 1').exists())

    def test_completed_todo_view_valid_id(self):
        # Test adding a valid todo item.
        response = self.client.post(reverse(addTodoItem), {'text':'New Task'})
        self.assertEqual(response.status_code, 302) # Redirect to index
        self.assertEqual(Todolist.objects.count(), 4)# Three initial + one new
        self.assertTrue(Todolist.objects.filter(text='New Task').exists())

    def test_add_todo_item_invalid(self):
        # Test adding an invalid todo item (empty text).
        response = self.client.post(reverse(addTodoItem), {'text': ''})
        self.assertEqual(response.status_code, 302) # Redirect to index
        self.assertEqual(Todolist.objects.count(), 3)# No new task should be added

    def test_completed_todo_valid(self):
        # Test marking a valid todo item as completed.
        response = self.client.post(reverse(completedTodo,args=[self.task1.id]))
        self.assertEqual(response.status_code, 302) # Redirect to index
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.completed)