from rest_framework import serializers
from django.utils import timezone
from .models import Book, Publisher
from .validators import validate_title_length


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(validators=[validate_title_length])
    amount_pages = serializers.IntegerField()

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['created_at', 'id']


    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        return super().create(validated_data)
    

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].strip().title()

        return super().update(instance, validated_data)
    

    def validate_amount_pages(self, value):
        if value < 1:
            raise serializers.ValidationError('Amount of pages cant be less then 1.')
        return value
    

    def validate(self, data):
        if data.get('discounted_price') and data.get('price'):
            if data['discounted_price'] > data['price']:
                raise serializers.ValidationError('Discounted price cant be higher then regular price.')
            
        return data
    

class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = '__all__'

