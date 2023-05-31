from django.contrib.auth.models import User
from django.db import models


class Events(models.Model):
    title = models.CharField('Название', max_length=50)
    announcement = models.CharField('Анонс', max_length=250)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата проведения')
    place = models.CharField('Примерное местоположение', max_length=50)
    image = models.ImageField(upload_to='event_preview/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/events/{self.id}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Featured(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    event = models.ManyToManyField(Events)

    def __str__(self):
        return self.event


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Events, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wished_item

    class Meta:
        verbose_name = 'Желаемое'
        verbose_name_plural = 'Список желаемого'


class Review(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    comment = models.TextField('Комментарий')
    date = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="review")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
