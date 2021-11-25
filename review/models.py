from django.core.validators import MaxValueValidator
from django.db import models

from account.models import CustomUser
from cinema.models import Movie
from django.contrib.auth.models import AnonymousUser


class Review(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name='Product', on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(verbose_name='Добавить отзыв:')
    verified = models.BooleanField(blank=True, default=False)
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)], default=11)



    def __str__(self):
        return f'{self.name} - {self.created}'




