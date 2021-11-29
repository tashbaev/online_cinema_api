from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters


from .models import Movie
from .serializers import MovieSerializer


class MovieFilter(filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['categories',]


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['title', 'description']
    ordering_fields = ['reviews__rate', 'upload_time']

