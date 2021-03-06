# Generated by Django 3.2.9 on 2021-11-24 11:38

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(verbose_name='Добавить отзыв:')),
                ('verified', models.BooleanField(blank=True, default=False)),
                ('rate', models.PositiveSmallIntegerField(default=11, validators=[django.core.validators.MaxValueValidator(10)])),
                ('author', models.ForeignKey(default=django.contrib.auth.models.AnonymousUser, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cinema.movie', verbose_name='Product')),
            ],
        ),
    ]
