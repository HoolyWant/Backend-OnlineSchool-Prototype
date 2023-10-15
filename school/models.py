from django.db import models, connection

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} CASCADE')


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link = models.CharField(max_length=200, verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE, related_name='lesson')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} CASCADE;')


class Payment(models.Model):
    CASH = 'cash'
    CARD = 'card'
    PAYMENT_METHODS = ((CASH, 'наличные'),
                       (CARD, 'карта'))

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course,  on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson,  on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

    def __str__(self):
        return self.amount

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} CASCADE;'
                           f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY')


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    following_status = models.BooleanField(default=True, verbose_name='статус подписки')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f'{self.user}, {self.course}, {self.following_status}'
