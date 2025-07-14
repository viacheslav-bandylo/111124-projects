from django.urls import path
from .views import book_list_create, book_detail_update_delete, create_genre

urlpatterns = [
    path('books/', book_list_create, name='book-list-create'),  # Для получения всех книг и создания новой книги
    path('books/<int:pk>/', book_detail_update_delete, name='book-detail-update-delete'),  # Для операций с одной книгой
    path('genres/', create_genre, name='create-genre'), # Маршрут для создания жанра
]
