from django.test import TestCase
from tasks.forms import TaskForm
from tasks.models import Tag


class TaskFormTest(TestCase):
    def test_task_form_is_valid(self):
        tag = Tag.objects.create(name="test_Tag")
        form_data = {
            "content": "test_content",
            "is_done": False,
            "tags": [tag.id, ],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data["content"],
            form_data["content"]
        )
        self.assertEqual(form.cleaned_data["is_done"], False)
        self.assertTrue(tag in form.cleaned_data["tags"])
