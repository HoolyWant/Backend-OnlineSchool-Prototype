from django.db import models
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link = models.CharField(max_length=200, verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE, related_name='lesson')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title




