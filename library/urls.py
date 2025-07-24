from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import create_genre, BookListCreateView, BookDetailUpdateDeleteView, \
    ExpensiveBooksView, GenreDetailUpdateDeleteView, GenreViewSet, \
    books_by_date_view, lazy_load_demo, create_book_and_publisher_view, \
    ProtectedDataView, PublicView, AdminView, \
    ReadOnlyOrAuthenticatedView, UserBookListView  # book_list_create, book_detail_update_delete,

router = DefaultRouter()

router.register('genres', GenreViewSet)

urlpatterns = [
    # path('books/', book_list_create, name='book-list-create'),  # Для получения всех книг и создания новой книги
    # path('books/<int:pk>/', book_detail_update_delete, name='book-detail-update-delete'),  # Для операций с одной книгой
    # path('genres/', create_genre, name='create-genre'), # Маршрут для создания жанра
    # path('books/', BookListCreateView.as_view(), name='book-list-create'),  # Для получения всех книг и создания новой книги
    # path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),  # Для операций с одной книгой

    path('books/', BookListCreateView.as_view(), name='book-list-create'), # Для получения всех книг и создания новой книги
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'), # Для операций с одной книгой
    path('books/expensive/', ExpensiveBooksView.as_view(), name='book-expensive'),
    # path('genres/', create_genre, name='create-genre'), # Маршрут для создания жанра
    # path('genres/<str:name>/', GenreDetailUpdateDeleteView.as_view(), name='genre-detail-update-delete'),

    path('', include(router.urls)),
    re_path(r'^books/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', books_by_date_view, name='books-by-date'),
    path('lazy_load/', lazy_load_demo, name='lazy-load-demo'),
    path('books/transaction/', create_book_and_publisher_view, name='book-create-book-and-publisher'),
    path('user-books/', UserBookListView.as_view(), name='user-book-list'),

    path('protected/', ProtectedDataView.as_view(), name='protected-data'),
    path('public/', PublicView.as_view(), name='public-data'),
    path('for-admin/', AdminView.as_view(), name='admin-data'),
    path('read-anon/', ReadOnlyOrAuthenticatedView.as_view(), name='read-anon'),
]
