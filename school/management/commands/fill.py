from django.core.management import BaseCommand

from school.models import Payment, Course, Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.truncate_table_restart_id()
        courses_list = [
            {'title': 'Руби', 'description': 'Язык программирования'},
            {'title': 'Го', 'description': 'Язык программирования'},
            {'title': 'Джава', 'description': 'Язык программирования'},
            {'title': 'Питон', 'description': 'Язык программирования'},
        ]
        lessons_list = [
            {'title': 'Линукс', 'description': 'Операционная система',
             'link': 'здесь могла быть ваша ссылка на видео', 'course': "4"},
        ]
        payment_list = [
            {'course': '1', 'lesson': 'None', 'amount': '120000', 'payment_method': 'cash'},
            {'course': 'None', 'lesson': '1', 'amount': '5000', 'payment_method': 'cash'},
            {'course': '2', 'lesson': 'None', 'amount': '150000', 'payment_method': 'card'},
            {'course': '3', 'lesson': 'None', 'amount': '200000', 'payment_method': 'cash'},
            {'course': '4', 'lesson': 'None', 'amount': '135000', 'payment_method': 'card'},

        ]
        courses_for_create = []
        for course in courses_list:
            courses_for_create.append(
                Course(**course)
            )
        Course.objects.bulk_create(courses_for_create)

        for lesson in lessons_list:
            if lesson['course'] == 'None':
                course = None
            else:
                course = Course.objects.get(pk=lesson['course'])
            Lesson.objects.create(title=lesson['title'],
                                  description=lesson['description'],
                                  course=course,
                                  )

        for payment in payment_list:
            if payment['course'] == 'None':
                course = None
            else:
                course = Course.objects.get(pk=payment['course'])
            if payment['lesson'] == 'None':
                lesson = None
            else:
                lesson = Lesson.objects.get(pk=payment['lesson'])
            Payment.objects.create(course=course,
                                   lesson=lesson,
                                   amount=payment['amount'],
                                   payment_method=payment['payment_method'],
                                   )

