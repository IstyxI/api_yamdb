from django.core.mail import send_mail

# from api_yamdb.settings import EMAIL_HOST_USER


def send_confirmation_code(email, confirmation_code):
    """Oтправка кода подтверждения."""
    send_mail(
        subject='Код подтверждения',
        message=f'Ваш код: {confirmation_code}',
        from_email=None,
        recipient_list=(email,),
        fail_silently=False,
    )
