from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer, BookCreateSerializer, GenreSerializer

# @api_view(['GET', 'POST'])
# def book_list_create(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookListSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = BookCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class BookListCreateView(APIView, PageNumberPagination):
#     page_size = 2
#
#     def get(self, request):
#         #### Filter ####
#         filters = {}
#         title = request.query_params.get('title')
#         published_year = request.query_params.get('pub_year')
#
#         if title:
#             filters['title'] = title
#
#         if published_year:
#             filters['publication_date__year'] = published_year
#
#         books = Book.objects.filter(**filters)
#
#         #### Sorting ####
#
#         # Получаем параметр 'sort_by'. Если его нет, по умолчанию сортируем по 'title'.
#         sort_by = request.query_params.get('sort_by', 'title')
#         # Получаем параметр 'sort_order'. По умолчанию сортируем по возрастанию ('asc').
#         sort_order = request.query_params.get('sort_order', 'asc')
#
#         if sort_order == 'desc': # Если порядок сортировки 'desc' (убывание)...
#             sort_by = f'-{sort_by}' # ...добавляем минус перед именем поля для убывающей сортировки
#         books = books.order_by(sort_by) # Применяем сортировку
#
#         #### Pagination ####
#
#         requested_page_size = self.get_page_size(request)
#         self.page_size = requested_page_size
#
#         result = self.paginate_queryset(books, request, view=self)
#
#         serializer = BookListSerializer(result, many=True)
#         return self.get_paginated_response(serializer.data)
#
#     def get_page_size(self, request):
#         page_size_param = request.query_params.get('page_size')
#
#         if page_size_param and page_size_param.isdigit():
#             return int(page_size_param)
#
#         return self.page_size
#
#     def post(self, request):
#         serializer = BookCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookListCreateView(GenericAPIView):
#     # 1. Указываем, что мы работаем со всеми объектами модели Book
#     queryset = Book.objects.all()
#     # 2. Указываем, что для преобразования будем использовать BookSerializer
#     serializer_class = BookSerializer
#
#     # Метод для обработки GET-запроса (получение списка)
#     def get(self, request, *args, **kwargs):
#         # 1. Получаем набор всех книг с помощью встроенного метода
#         queryset = self.get_queryset()
#         # 2. Сериализуем набор объектов (many=True указывает, что объектов много)
#         serializer = self.get_serializer(queryset, many=True)
#         # 3. Возвращаем ответ в формате JSON
#         return Response(serializer.data)
#
#     # Метод для обработки POST-запроса (создание объекта)
#     def post(self, request, *args, **kwargs):
#         # 1. Передаем данные из запроса в сериализатор
#         serializer = self.get_serializer(data=request.data)
#         # 2. Проверяем, корректны ли данные. Если нет - вызовется исключение
#         serializer.is_valid(raise_exception=True)
#         # 3. Сохраняем новый объект в базу данных
#         serializer.save()
#         # 4. Возвращаем созданный объект и статус 201 CREATED
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# Этот класс заменяет наш BookListCreateView
# Он наследуется от ListCreateAPIView, который уже умеет:
# - обрабатывать GET для получения списка (List)
# - обрабатывать POST для создания объекта (Create)
class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Переопределяем метод create
    def create(self, request, *args, **kwargs):
        # Копируем данные из запроса, чтобы их можно было изменять
        data = request.data.copy()

        # Наша кастомная логика
        if 'author' not in data or not data['author']:
            data['author'] = 1

        # Дальше идет стандартная логика из DRF
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create вызывает serializer.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# # --- Представление для одного объекта (чтение, обновление, удаление) ---
# class BookDetailUpdateDeleteView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     # Метод для обработки GET-запроса (получение одного объекта)
#     def get(self, request, *args, **kwargs):
#         # 1. Получаем один конкретный объект по его pk (id) из URL
#         book = self.get_object()
#         # 2. Сериализуем его
#         serializer = self.get_serializer(book)
#         # 3. Возвращаем ответ
#         return Response(serializer.data)
#
#     # Метод для обработки PUT-запроса (полное обновление)
#     def put(self, request, *args, **kwargs):
#         book = self.get_object()
#         serializer = self.get_serializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     # Метод для обработки PATCH-запроса (частичное обновление)
#     def patch(self, request, *args, **kwargs):
#         book = self.get_object()
#         # partial=True говорит сериализатору, что обновление частичное
#         serializer = self.get_serializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     # Метод для обработки DELETE-запроса (удаление)
#     def delete(self, request, *args, **kwargs):
#         book = self.get_object()
#         book.delete()
#         # Возвращаем пустой ответ со статусом 204 NO CONTENT
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Этот класс заменяет наш BookDetailUpdateDeleteView
# Он наследуется от RetrieveUpdateDestroyAPIView, который умеет:
# - обрабатывать GET для получения одного объекта (Retrieve)
# - обрабатывать PUT/PATCH для обновления (Update)
# - обрабатывать DELETE для удаления (Destroy)
class BookDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail_update_delete(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = BookDetailSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = BookCreateSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# class BookDetailUpdateDeleteView(APIView):
#     def get(self, request, pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookDetailSerializer(book)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookCreateSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ExpensiveBooksView(ListAPIView):
    serializer_class = BookSerializer

    # Мы не указываем queryset, т.к. будем формировать его динамически
    # Вместо этого мы полностью переопределяем метод get_queryset
    def get_queryset(self):
        # 1. Вычисляем среднюю цену всех книг
        average_price = Book.objects.aggregate(avg_price=Avg('price'))['avg_price']

        if average_price is None:
            return Book.objects.none()  # Возвращаем пустой набор, если книг нет

        # 2. Возвращаем книги, цена которых выше средней
        return Book.objects.filter(price__gt=average_price)


@api_view(['POST'])
def create_genre(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Возвращаем ошибки, если данные некорректны
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
