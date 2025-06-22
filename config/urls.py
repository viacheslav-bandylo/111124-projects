from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('project/', include('project.urls')),
    path('taskmanager/', include('TaskManager.urls')),
]