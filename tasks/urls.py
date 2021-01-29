from django.urls import path, include

import tasks.views


urlpatterns = [
    path('', tasks.views.index, name='index'),  # show the next task
    path('list/', tasks.views.TaskListView.as_view(), name='tasks'),
    # task detail
    # 
]
