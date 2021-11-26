from django.conf import settings
from django.core.mail import send_mail

def send_activation_code(email, activation_code):
    activation_url = f"http://localhost:8000/account/activate/{activation_code}"
    message = f"Thanks for registration. To activate your account go through the link: {activation_url}"
    email_from = settings.EMAIL_HOST_USER
    print(message)
    send_mail(
        'Activate your account.',
        message,
        'test@test.com',
        [email, ],
        fail_silently=False,
    )
