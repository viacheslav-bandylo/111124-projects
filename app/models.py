from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Author(models.Model):

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")
    profile = models.URLField(null=True, blank=True, verbose_name="Ссылка на профиль")
    deleted = models.BooleanField(default=False, verbose_name="Удалён ли автор",
                                  help_text = "Если False - автор активен. Если True - автора \ больше нет в списке доступных")
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг автора")