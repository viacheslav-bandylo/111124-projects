from django.urls import path
from .views import create_genre, BookListCreateView, BookDetailUpdateDeleteView, \
    ExpensiveBooksView, GenreDetailUpdateDeleteView  # book_list_create, book_detail_update_delete,

urlpatterns = [
    # path('books/', book_list_create, name='book-list-create'),  # Для получения всех книг и создания новой книги
    # path('books/<int:pk>/', book_detail_update_delete, name='book-detail-update-delete'),  # Для операций с одной книгой
    # path('genres/', create_genre, name='create-genre'), # Маршрут для создания жанра
    # path('books/', BookListCreateView.as_view(), name='book-list-create'),  # Для получения всех книг и создания новой книги
    # path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),  # Для операций с одной книгой

    path('books/', BookListCreateView.as_view(), name='book-list-create'), # Для получения всех книг и создания новой книги
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'), # Для операций с одной книгой
    path('books/expensive/', ExpensiveBooksView.as_view(), name='book-expensive'),
    path('genres/', create_genre, name='create-genre'), # Маршрут для создания жанра
    path('genres/<str:name>/', GenreDetailUpdateDeleteView.as_view(), name='genre-detail-update-delete'),
]
