from django.shortcuts import render
from django.views import generic

from tasks.models import Task


def index(request):
    """View function for home page of site."""

    tasks = Task.objects
    num_tasks = tasks.count()
    num_done = tasks.filter(done__exact=True).count()

    context = {
        "num_tasks": num_tasks,
        "num_done": num_done,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "tasks/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
