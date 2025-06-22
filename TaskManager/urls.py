from django.urls import path
from TaskManager.views import (
    create_task,
    create_subtask,
    read_task,
    read_subtask,
    update_task,
    update_subtask,
    delete_task,
)

urlpatterns = [
    path('create_task', view=create_task),
    path('create_subtask', view=create_subtask),
    path('read_task', view=read_task),
    path('read_subtask', view=read_subtask),
    path('update_task', view=update_task),
    path('update_subtask', view=update_subtask),
    path('delete_task', view=delete_task),
]