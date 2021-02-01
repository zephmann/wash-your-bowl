import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse



class Project(models.Model):
    """High-level group of tasks."""
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("project-detail", args=[str(self.pk)])

    def __str__(self):
        return self.name


class Category(models.Model):
    """Category for organizing tasks."""
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("category-detail", args=[str(self.pk)])

    def __str__(self):
        return self.name


class Task(models.Model):
    """A single task."""
    text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    blockers = models.ManyToManyField(
        "self", blank=True,
        related_name="dependents",
        symmetrical=False,
    )

    created_date = models.DateField(default=datetime.date.today)
    finished_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["done", "blocked"]

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self._done = self.done

    def save(self, *args, **kwargs):
        try:
            self.blocked = bool(self.blockers.count())
        except ValueError:
            pass

        if not self._done and self.done:
            self.finished_date = datetime.date.today()
            self._done = True

            try:
                # unblock any dependents
                for dependent in self.dependents.all():
                    dependent.blockers.remove(self)
                    dependent.save()
            except ValueError:
                pass

        super(Task, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("task-detail", args=[str(self.pk)])

    def __str__(self):
        return self.text
