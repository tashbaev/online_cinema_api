import django_rest_passwordreset
from django.urls import path, include

from .views import RegisterView, ActivateView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]

