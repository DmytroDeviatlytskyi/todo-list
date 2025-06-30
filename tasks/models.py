from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=63)
    date = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-date"]

    def __str__(self):
        return self.content
