from django.urls import path

from .views import ReviewCreateView, ReviewUpdateDeleteView, LikeCreateView, LikeDeleteView

urlpatterns = [
    path('create/<int:movie_id>/', ReviewCreateView.as_view()),
    path('<int:pk>/', ReviewUpdateDeleteView.as_view()),
    path('likes/<int:review_id>/', LikeCreateView.as_view()),
    path('like/<int:pk>/', LikeDeleteView.as_view())

]