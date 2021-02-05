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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        task_list = context.pop("task_list")

        context["active_tasks"] = []
        context["blocked_tasks"] = []
        context["done_tasks"] = []

        # TODO faster to do 3 queries?
        for task in task_list:
            if task.done:
                context["done_tasks"].append(task)
            elif task.blocked:
                context["blocked_tasks"].append(task)
            else:
                context["active_tasks"].append(task)
        
        return context


class TaskDetailView(generic.DetailView):
    model = Task


class ProjectDetailView(generic.DetailView):
    model = Project


class CategoryDetailView(generic.DetailView):
    model = Category
