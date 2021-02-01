from django.urls import path, include

import tasks.views


urlpatterns = [
    path("", tasks.views.index, name='index'),  # show the next task
    path("list/", tasks.views.TaskListView.as_view(), name="tasks"),
    path(
        "task/<int:pk>/", 
        tasks.views.TaskDetailView.as_view(), 
        name="task-detail"
    ),
    path(
        "project/<int:pk>/", 
        tasks.views.ProjectDetailView.as_view(), 
        name="project-detail"
    ),
    path(
        "category/<int:pk>/", 
        tasks.views.CategoryDetailView.as_view(), 
        name="category-detail"
    ),
    # project list
    # project detail (all tasks in project)
    # category list
    # category detail (all tasks in category)
]
