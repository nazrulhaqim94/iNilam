from traceback import print_tb
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Books
from .serializers import BooksSerializersInput, BooksSerializers, BooksSerializersAll, BooksSerializersUID
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Books, LANGUAGE, TAGS
from django.db.models import Count

# Create your views here.

class BookInputView(APIView):

    def get_object(self, id):
        try:
            return Books.objects.get(created_by=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        
        serializers = BooksSerializersInput(data=request.data)
        user = self.request.user

        try:
            if serializers.is_valid():
                serializers.save(created_by=user, approval_status='Pending Approval')

                return Response({'success': 'Buku Ditambah'})
            else:
                return Response({'error': 'Sesuatu telah berlaku'})
        except:
            return Response({'error': 'Sesuatu telah berlaku'})

    def get(self, request):
        books = Books.objects.all()
        serializers = BooksSerializersAll(books, many=True)
        return Response(serializers.data)

class BookGetByID(APIView):
    def get_object(self, id):
        try:
            return Books.objects.get(uid=id)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        books = self.get_object(id)
        serializers = BooksSerializers(books)
        return Response(serializers.data)
    
    def put(self, request, id):
        data = request.data
        print(data)
        if Books.objects.filter(uid=id).exists():
            book = self.get_object(id)
            serializer = BooksSerializersUID(book, data=request.data)
            if serializer.is_valid():
                serializer.save(approval_status='Pending Approval')
            return Response({'success': 'Buku Dikemaskini'})
        else:
            return Response({'error': 'Buku gagal dikemaskini'})

class BookGetByIDTeacher(APIView):
    def get_object(self, id):
        try:
            return Books.objects.get(uid=id)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        books = self.get_object(id)
        serializers = BooksSerializers(books)
        return Response(serializers.data)
    
    def put(self, request, id):
        data = request.data
        print(data)
        if Books.objects.filter(uid=id).exists():
            book = self.get_object(id)
            serializer = BooksSerializersUID(book, data=data)
            if serializer.is_valid():
                serializer.save(approval_status="Comment Added")
            return Response({'success': 'Komen Ditambah'})
        else:
            return Response({'error': 'Gagal dikemaskini'})

class BookGetByIDApproval(APIView):
    def get_object(self, id):
        try:
            return Books.objects.get(uid=id)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        data = request.data
        print(data)
        if Books.objects.filter(uid=id).exists():
            book = self.get_object(id)
            serializer = BooksSerializersUID(book, data=request.data)
            if serializer.is_valid():
                serializer.save(approval_status="Approved")
            return Response({'success': 'Diluluskan'})
        else:
            return Response({'error': 'Tidak Diluluskan'})

class LangChoicesView(APIView):
    def get(self, request, format=None):

        my_choices = []
        choice_dict = dict(LANGUAGE)
        for key, value in choice_dict.items():

            itered_dict = {"key": key, "value": value}
            my_choices.append(itered_dict)
        return Response(my_choices, status=status.HTTP_200_OK)

class TagChoicesView(APIView):
    def get(self, request, format=None):

        my_choices = []
        choice_dict = dict(TAGS)
        for key, value in choice_dict.items():

            itered_dict = {"key": key, "value": value}
            my_choices.append(itered_dict)
        return Response(my_choices, status=status.HTTP_200_OK)

class RankingStudentView(APIView):
    def get(self, request):
        test = Books.objects.filter(approval_status="Approved").values("created_by").annotate(book_count=Count('pk')).order_by('created_by')

        return Response(test, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        
        data = self.request.data
        month = data["getMonth"]
        year = data["getYear"]
        print(month, year)
        
        filtered_data = Books.objects.filter(date_read__month=month, date_read__year=year, approval_status="Approved").values("created_by").annotate(book_count=Count('pk')).order_by('created_by')

        print(filtered_data)

        return Response(filtered_data, status=status.HTTP_200_OK)


