from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

# @receiver - это декоратор для подключения функции к сигналу
# Первый аргумент - сам сигнал (post_save)
# sender=Book - указывает, что мы слушаем сигнал только от модели Book
@receiver(post_save, sender=Book)
def book_saved_handler(sender, instance, created, **kwargs):
    # 'created' - это флаг, который говорит нам, был ли объект создан
    if created:
        print(f'Новая книга создана: {instance.title}')
    else:
        print(f'Книга обновлена: {instance.title}')


@receiver(post_save, sender=Book)
def notify_admin_on_new_book(sender, instance, created, **kwargs):
    if created:
        print("Отправка письма администратору...")
        send_mail(
            subject=f'Новая книга в системе: {instance.title}',
            message=f'Пользователь {instance.owner.username} добавил новую книгу "{instance.title}" (ID: {instance.id}).',
            from_email='noreply@example.com',
            recipient_list=['admin@example.com'],
        )


# def book_saved_handler(sender, instance, created, **kwargs):
#     if created:
#         print(f'Новая книга создана: {instance.title}')
#     else:
#         print(f'Книга обновлена: {instance.title}')
#
# # Подключаем функцию к сигналу вручную
# post_save.connect(book_saved_handler, sender=Book)