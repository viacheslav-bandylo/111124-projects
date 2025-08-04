from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from config import settings


# Создаем "вид" нашей схемы документации
schema_view = get_schema_view(
   openapi.Info(
      title="My Project API",
      default_version='v1',
      description="API documentation for my awesome project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Маршруты для документации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('project/', include('project.urls')),
    path('taskmanager/', include('TaskManager.urls')),

    path('shop/', include('shop.urls')),

    # Маршрут для получения access и refresh токенов
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Маршрут для обновления access токена с помощью refresh токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('get-token/', obtain_auth_token, name='get_token'), # Маршрут для получения токена
]


urlpatterns += i18n_patterns(
    path('library/', include('library.urls')),
    prefix_default_language=False,
)
