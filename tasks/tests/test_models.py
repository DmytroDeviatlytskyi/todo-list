from django.test import TestCase

from tasks.models import Task, Tag


class TagTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            name="test_tag"
        )

    def test_create_tag(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.name, "test_tag")

    def test_tag_str(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(str(tag), tag.name)


class TaskTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            name="test_tag"
        )
        test_task = Task.objects.create(
            content="test_content",
        )
        tags = Tag.objects.all()
        test_task.tags.set(tags)
        test_task.save()

    def test_create_task(self):
        task = Task.objects.get(id=1)
        tags = task.tags.all()
        self.assertEqual(task.content, "test_content")
        self.assertEqual(list(task.tags.all()), list(tags))

    def test_task_str(self):
        task = Task.objects.get(id=1)
        self.assertEqual(str(task), task.content)
