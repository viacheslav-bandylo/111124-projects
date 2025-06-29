from django.urls import path
from project.views import test, list_projects, list_tasks

urlpatterns = [
    path('test', view=test),
    path('project', view=list_projects),
    path('task', view=list_tasks),
]