from django.urls import path
from project.views import test

urlpatterns = [
    path('test', view=test)
]