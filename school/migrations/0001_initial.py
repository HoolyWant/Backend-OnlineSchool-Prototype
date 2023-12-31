# Generated by Django 4.2.6 on 2023-10-14 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('description', models.TextField(verbose_name='описание')),
                ('link', models.CharField(max_length=200, verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('amount', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('card', 'карта')], max_length=10, verbose_name='способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.course', verbose_name='курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.lesson', verbose_name='урок')),
            ],
            options={
                'verbose_name': 'оплата',
                'verbose_name_plural': 'оплаты',
            },
        ),
    ]
