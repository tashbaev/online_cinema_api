from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from django.dispatch import receiver
from django.shortcuts import render
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer
from .utils import send_reset_code


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Successfully Signed Up!!!", status=status.HTTP_201_CREATED)


# class ChangePassword(PasswordResetView):



class ActivateView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response("Your account successfully activated!!!", status=status.HTTP_200_OK)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully logged out', status=status.HTTP_200_OK)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    """
      Handles password reset tokens
      When a token is created, an e-mail needs to be sent to the user
    """
    # send an e-mail to the user

    context = {
        'email': reset_password_token.user.email,
        'reset_password_url': reset_password_token.key,
    }
    print(context)
    send_reset_code.delay(context)

