from rest_framework import mixins
from rest_framework.generics import GenericAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Review, Likes
from .permissions import IsAuthorPermission
from .serializers import ReviewSerializer, LikesSerializer


class ReviewCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated,]

    queryset = Review.objects.all().order_by('likes__count')
    serializer_class = ReviewSerializer


class ReviewUpdateDeleteView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    permission_classes = [IsAuthorPermission,]
    queryset = Review.objects.all().order_by('likes__count')
    serializer_class = ReviewSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class LikeCreateView(mixins.CreateModelMixin, GenericAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LikeDeleteView(DestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer





