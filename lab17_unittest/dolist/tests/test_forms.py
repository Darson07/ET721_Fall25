from django.test import TestCase
from dolist.forms import TodoListForm

class TodoListFormTest(TestCase):
    def test_todo_list_form_valid_data(self):
        form = TodoListForm(data={'text': 'Buy groceries'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['text'], 'Buy groceries')

    def test_todo_list_form_empty_data(self):
        form = TodoListForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('text', form.errors)
        self.assertEqual(form.errors['text'], ['This field is required.'])

    def test_todo_list_form_max_length_exceeded(self):
        form = TodoListForm(data={'text': 'a' * 46}) # Exceed max length
        self.assertFalse(form.is_valid())
        self.assertIn('text', form.errors)
        self.assertEqual(form.errors['text'], ['Ensure this value has at most 45 characters (it has 46).'])

    def test_todo_list_form_widget_attributes(self):
        form = TodoListForm()
        self.assertIn('class', form.fields['text'].widget.attrs)
        self.assertEqual(form.fields['text'].widget.attrs['class'],
        'todo_text')
        self.assertIn('placeholder', form.fields['text'].widget.attrs)
        self.assertEqual(form.fields['text'].widget.attrs['placeholder'],
        'type your task...')
        self.assertIn('aria-label', form.fields['text'].widget.attrs)
        self.assertEqual(form.fields['text'].widget.attrs['aria-label'],
        'task')
        self.assertIn('aria-describeby', form.fields['text'].widget.attrs)
        self.assertEqual(form.fields['text'].widget.attrs['aria-describeby'],
        'btn-add')