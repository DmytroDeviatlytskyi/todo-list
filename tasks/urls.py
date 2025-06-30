from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/", TagListView.as_view(), name="tag-list")
]
