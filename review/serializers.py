from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from cinema.models import Movie
from .models import Review, Likes


class LikesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    review = serializers.ReadOnlyField(source='review.id')

    class Meta:
        model = Likes
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        review_id = self.context.get('view').kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        like = Likes.objects.create(author=author, review=review, **validated_data)
        return like



class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    movie = serializers.ReadOnlyField(source='movie.id')

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        movie_id = self.context.get('view').kwargs.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        # movie = Movie.objects.filter(id=movie_id)[0]
        # print(movie)
        review = Review.objects.create(author=author, movie=movie, **validated_data)
        return review

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.count()
        representation['author'] = instance.author.email

        return representation



    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['rating'] = instance.rate.avg()


