from django.db.models import Avg
from rest_framework import serializers

from review.serializers import ReviewSerializer, ReviewSerializerS
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ['favorites',]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['favorites_on'] = instance.favorites.count()
        representation.update(instance.reviews.exclude(rate=None).aggregate(Avg('rate')))
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        # print(instance.reviews.all())
        return representation