from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.urls import reverse

class Mail:

    @staticmethod
    def get_absolute_url(url):
        if settings.DEBUG: #EN MODO DESARROLLO
            return 'http://localhost:8000{}'.format(
                reverse(url)
            )

    @staticmethod
    def send_complete_order(name,email,text):
        subject = "White House:Nuevo mensaje de contacto",
        template = get_template('mails/completed.html')
        content = template.render({
            'user':name,
        })

        message = EmailMultiAlternatives(subject,
                                        'Mensaje importante',
                                        settings.EMAIL_HOST_USER,
                                        [email]
        )

        message.attach_alternative(content, 'text/html')
        message.send()
