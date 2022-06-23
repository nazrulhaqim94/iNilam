from rest_framework import serializers
from .models import Books

class BooksSerializersInput(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('book_title', 'book_author', 'date_published','date_read', 'page', 'language', 'tags', 'summary')

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('book_title', 'book_author', 'date_published','date_read', 'page', 'language', 'tags', 'summary', 'comment')

class BooksSerializersAll(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class BooksSerializersUID(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id','book_title', 'book_author', 'date_published','date_read', 'page', 'language', 'tags', 'summary', 'comment')