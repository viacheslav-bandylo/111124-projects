from django.urls import path
from app.views import hello_user

urlpatterns = [path("hello", view=hello_user, name="hello_user")]