from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, GenreSerializer

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
    

class BookListCreateView(APIView, PageNumberPagination):
    page_size = 2

    def get(self, request):
        #### Filter ####
        filters = {}
        title = request.query_params.get('title')
        published_year = request.query_params.get('pub_year')

        if title:
            filters['title'] = title

        if published_year:
            filters['publication_date__year'] = published_year

        books = Book.objects.filter(**filters)

        #### Sorting ####

        # Получаем параметр 'sort_by'. Если его нет, по умолчанию сортируем по 'title'.
        sort_by = request.query_params.get('sort_by', 'title')
        # Получаем параметр 'sort_order'. По умолчанию сортируем по возрастанию ('asc').
        sort_order = request.query_params.get('sort_order', 'asc')

        if sort_order == 'desc': # Если порядок сортировки 'desc' (убывание)...
            sort_by = f'-{sort_by}' # ...добавляем минус перед именем поля для убывающей сортировки
        books = books.order_by(sort_by) # Применяем сортировку

        #### Pagination ####

        requested_page_size = self.get_page_size(request)
        self.page_size = requested_page_size

        result = self.paginate_queryset(books, request, view=self)

        serializer = BookListSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)
    
    def get_page_size(self, request):
        page_size_param = request.query_params.get('page_size')

        if page_size_param and page_size_param.isdigit():
            return int(page_size_param)
        
        return self.page_size
    
    def post(self, request):
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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

class BookDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookCreateSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_genre(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Возвращаем ошибки, если данные некорректны
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
