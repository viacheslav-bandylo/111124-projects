from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

import pytest
from .models import SimpleBook

# Пометка, которая говорит pytest, что этот тест может работать с базой данных
@pytest.mark.django_db
def test_simple_book_model():
    """
    Тест для проверки создания объекта книги и работы кастомного метода is_classic().
    """
    # 1. Arrange (Подготовка): Создаем объект в памяти
    book = SimpleBook.objects.create(
        title="Война и мир",
        author="Лев Толстой",
        publication_year=1869
    )

    # 2. Act (Действие) & Assert (Проверка)
    # Проверяем, что объект создался и его поля соответствуют ожидаемым
    assert book.title == "Война и мир"
    assert str(book) == "Война и мир" # Проверяем работу метода __str__

    # Проверяем наш кастомный метод
    assert book.is_classic() is True

    # Создадим другую книгу для проверки обратного случая
    book_modern = SimpleBook.objects.create(
        title="Гарри Поттер и философский камень",
        author="Дж. К. Роулинг",
        publication_year=1997
    )
    # В этом примере она тоже будет классикой, поменяем на более новый год
    book_modern.publication_year = 2007
    assert book_modern.is_classic() is False


class BookAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Этот метод вызывается один раз перед запуском всех тестов в классе.
        Идеально для создания объектов, которые не будут меняться.
        """
        cls.book1 = SimpleBook.objects.create(
            title="Преступление и наказание",
            author="Фёдор Достоевский",
            publication_year=1866
        )
        cls.book2 = SimpleBook.objects.create(
            title="Мастер и Маргарита",
            author="Михаил Булгаков",
            publication_year=1967
        )
        cls.list_url = reverse('simple-book-list-create') # Получаем URL по его имени

    def test_get_book_list(self):
        """
        Тест для GET-запроса (получение списка книг)
        """
        # Отправляем GET-запрос к нашему API
        response = self.client.get(self.list_url)

        # Проверяем, что ответ имеет статус-код 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе 2 объекта
        self.assertEqual(len(response.data.get('results')), 2)

        # Проверяем, что данные одной из книг соответствуют ожиданиям
        self.assertEqual(response.data.get('results')[0]['title'], self.book1.title)

    def test_create_book(self):
        """
        Тест для POST-запроса (создание новой книги)
        """
        # Данные для новой книги
        data = {
            "title": "Собачье сердце",
            "author": "Михаил Булгаков",
            "publication_year": 1925
        }

        # Отправляем POST-запрос
        response = self.client.post(self.list_url, data, format='json')

        # Проверяем, что ответ имеет статус-код 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяем, что количество книг в базе данных увеличилось на 1
        self.assertEqual(SimpleBook.objects.count(), 3)

        # Проверяем, что созданная книга имеет правильный заголовок
        new_book = SimpleBook.objects.get(id=response.data['id'])
        self.assertEqual(new_book.title, "Собачье сердце")
