from django.shortcuts import render
from django.views import generic

from tasks.models import Task, Project, Category


def index(request):
    """View function for home page of site."""

    tasks = Task.objects
    next_task = Task.objects.filter(done__exact=False, blocked__exact=False)
    next_task = next_task.order_by("?").first()

    num_tasks = tasks.count()
    num_done = tasks.filter(done__exact=True).count()

    context = {
        "next_task": next_task,
        "num_tasks": num_tasks,
        "num_done": num_done,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "tasks/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task


class ProjectDetailView(generic.DetailView):
    model = Project


class CategoryDetailView(generic.DetailView):
    model = Category
