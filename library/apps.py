from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "library"


    # Этот метод вызывается, когда Django полностью загрузит приложение
    def ready(self):
        import library.signals  # Импортируем наш модуль с сигналами
