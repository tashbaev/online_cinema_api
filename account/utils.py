from django.conf import settings
from django.core.mail import send_mail
from online_cinema_api.celery import app

@app.task
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


@app.task
def send_reset_code(context):
    reset_url = context.get('reset_password_url')
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
