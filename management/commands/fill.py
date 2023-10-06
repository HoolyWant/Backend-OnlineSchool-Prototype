from django.core.management import BaseCommand

from school.models import Payment, Course, Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):
        Course.truncate_table_restart_id()
        courses_list = [
            {'title': 'Руби', 'description': 'Язык программирования'},
            {'title': 'Го', 'description': 'Язык программирования'},
            {'title': 'Джава', 'description': 'Язык программирования'},
            {'title': 'Питон', 'description': 'Язык программирования'},
        ]
        courses_for_create = []
        for course in courses_list:
            courses_for_create.append(
                Course(**course)
            )

        Course.objects.bulk_create(courses_for_create)

        Lesson.truncate_table_restart_id()
        lessons_list = [
            {'title': 'Линукс', 'description': 'Операционная система',
             'link': 'здесь могла быть ваша ссылка на видео', 'course': '4'},

        ]
        lessons_for_create = []
        for lesson in lessons_list:
            lessons_for_create.append(
                Lesson(**lesson)
            )

        Lesson.objects.bulk_create(lessons_for_create)

        Payment.truncate_table_restart_id()
        payment_list = [
            {'course': 'Руби', 'amount': '120000', 'payment_method': 'cash'},
            {'lesson': 'Линукс', 'amount': '5000', 'payment_method': 'cash'},
            {'course': 'Го', 'amount': '150000', 'payment_method': 'card'},
            {'course': 'Джава', 'amount': '200000', 'payment_method': 'cash'},
            {'course': 'Питон', 'amount': '135000', 'payment_method': 'card'},

        ]
        payments_for_create = []
        for payment in payment_list:
            payments_for_create.append(
                Payment(**payment)
            )

        Payment.objects.bulk_create(payments_for_create)
