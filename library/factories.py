import factory

from library.models import SimpleBook


class SimpleBookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SimpleBook

    title = factory.Faker('sentence', nb_words=4) # Генерирует случайное предложение
    author = factory.Faker('name') # Генерирует случайное имя
    publication_date = factory.Faker('date')
