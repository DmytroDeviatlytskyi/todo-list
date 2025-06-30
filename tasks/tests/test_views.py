from django.test import TestCase
from django.urls import reverse, reverse_lazy
from tasks.models import Task, Tag

TASK_LIST_URL = reverse("tasks:task-list")
TASK_CREATE_URL = reverse("tasks:task-create")
TASK_UPDATE_URL = reverse("tasks:task-update", kwargs={"pk": 1})
TASK_DELETE_URL = reverse("tasks:task-delete", kwargs={"pk": 1})

TAG_LIST_URL = reverse("tasks:tag-list")
TAG_CREATE_URL = reverse("tasks:tag-create")
TAG_UPDATE_URL = reverse("tasks:tag-update", kwargs={"pk": 1})
TAG_DELETE_URL = reverse("tasks:tag-delete", kwargs={"pk": 1})


class TaskViewTests(TestCase):
    def setUp(self):
        Task.objects.create(
            content="Test_task_1",
        ),
        Task.objects.create(
            content="Test_task_2",
        ),

    def test_task_list_view(self):
        response = self.client.get(TASK_LIST_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["task_list"]), list(tasks))
        self.assertTemplateUsed(response, "tasks/task_list.html")

    def test_task_create_view(self):
        response = self.client.get(TASK_CREATE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_form.html")

    def test_task_update_view(self):
        response = self.client.get(TASK_UPDATE_URL)
        task = Task.objects.get(id=1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["task"], task)
        self.assertTemplateUsed(response, "tasks/task_form.html")

    def test_task_delete_view(self):
        response = self.client.get(TASK_DELETE_URL)
        task = Task.objects.get(id=1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["task"], task)
        self.assertTemplateUsed(response, "tasks/task_confirm_delete.html")


class TagViewTests(TestCase):
    def setUp(self):
        Tag.objects.create(name="Test_tag_1")
        Tag.objects.create(name="Test_tag_2")

    def test_tag_list_view(self):
        response = self.client.get(TAG_LIST_URL)
        tags = Tag.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tag_list"]), list(tags))
        self.assertTemplateUsed(response, "tasks/tag_list.html")

    def test_tag_create_view(self):
        response = self.client.get(TAG_CREATE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/tag_form.html")

    def test_tag_update_view(self):
        response = self.client.get(TAG_UPDATE_URL)
        tag = Tag.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"], tag)
        self.assertTemplateUsed(response, "tasks/tag_form.html")

    def test_tag_delete_view(self):
        response = self.client.get(TAG_DELETE_URL)
        tag = Tag.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"], tag)
        self.assertTemplateUsed(response, "tasks/tag_confirm_delete.html")


class TaskStatusViewTests(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(
            content="Test_task_1",
            is_done=False,
        )
        self.task2 = Task.objects.create(
            content="Test_task_2",
            is_done=True,
        )

    def test_task_status_view_false(self):
        response = self.client.get(
            reverse_lazy(
                "tasks:task-status", kwargs={"pk": self.task1.pk}
            )
        )
        self.assertRedirects(response, reverse_lazy("tasks:task-list"))

        self.task1.refresh_from_db()
        self.assertTrue(self.task1.is_done)

    def test_task_status_view_true(self):
        response = self.client.get(
            reverse_lazy(
                "tasks:task-status", kwargs={"pk": self.task2.pk}
            )
        )
        self.assertRedirects(response, reverse_lazy("tasks:task-list"))

        self.task2.refresh_from_db()
        self.assertFalse(self.task2.is_done)
