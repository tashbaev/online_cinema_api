from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters


from .models import Movie
from .serializers import MovieSerializer


class PermissionMixin:
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'delete', 'create']:
            permissions = [IsAdminUser,]
        else:
            permissions = []
        return [permission() for permission in permissions]


class MovieFilter(filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['categories',]


class MovieViewSet(PermissionMixin, ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['title', 'description']
    ordering_fields = ['reviews__rate', 'upload_time']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        # print(self.action)
        return context

