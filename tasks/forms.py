from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        required=False, widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        )
    )

    class Meta:
        model = Task
        fields = "__all__"
