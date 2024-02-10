from django.core.management import BaseCommand
from users_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='ilya.kalberdin@yandex.ru',
            first_name='Ilya',
            last_name='Kalberdin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345')
        user.save()
