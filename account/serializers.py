from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser
from .utils import send_activation_code


class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'password_confirm',)

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match!!!')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        username = validated_data.get('username')
        user = CustomUser.objects.create_user(email=email, username=username, password=password)
        # print(f"COOOOooode:::: {user.activation_code}")
        send_activation_code.delay(email=user.email, activation_code=user.activation_code)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                message = 'Unable log in with provided data!'
                raise serializers.ValidationError(message, code='authorization')

        else:
            message = 'Must have both email and password'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs

