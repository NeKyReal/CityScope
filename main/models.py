from django.db import models


class Contact(models.Model):
    name = models.CharField('Введите ваше имя', max_length=100)
    email = models.EmailField('Введите email-адрес')
    message = models.TextField('Ваш отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Обратная связь'

