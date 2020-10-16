from django.shortcuts import render
from rest_framework import generics
from .serializers import BooksSerializer
from .models import Books


# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer