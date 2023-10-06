from django.db import models
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link = models.CharField(max_length=200, verbose_name='ссылка')




