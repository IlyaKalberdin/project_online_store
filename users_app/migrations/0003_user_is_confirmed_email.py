# Generated by Django 5.0 on 2024-02-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_alter_user_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_confirmed_email',
            field=models.BooleanField(default=False, verbose_name='почта подтверждена'),
        ),
    ]