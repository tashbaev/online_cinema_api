from django.conf import settings
from django.core.mail import send_mail

def send_activation_code(email, activation_code):
    activation_url = f"http://localhost:8000/api/v1/account/activate/{activation_code}"
    message = f"Thanks for registration. To activate your account go through the link: {activation_url}"
    email_from = settings.EMAIL_HOST_USER
    # print(message)
    send_mail(
        'Activate your account.',
        message,
        'test@test.com',
        [email, ],
        fail_silently=False,
    )


def send_reset_code(context):
    reset_url = f"http://localhost:8000/api/v1/account/password_reset/{context.get('reset_code')}"
    message = f"To reset password go through the link: {reset_url}"
    email_from = settings.EMAIL_HOST_USER
    # print(message)
    send_mail(
        'Reset password url',
        message,
        'test@test.com',
        [context.get('email'), ],
        fail_silently=False,
    )
