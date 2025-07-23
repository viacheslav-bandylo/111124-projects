from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('project/', include('project.urls')),
    path('taskmanager/', include('TaskManager.urls')),
    path('library/', include('library.urls')),

    path('shop/', include('shop.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]