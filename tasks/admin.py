from django.contrib import admin

from tasks.models import Tag, Task


@admin.register(Task)
class TagAdmin(admin.ModelAdmin):
    list_display = ("content", "deadline", "is_done")
    search_fields = ("content",)
    list_filter = ("tags",)


admin.site.register(Tag)
