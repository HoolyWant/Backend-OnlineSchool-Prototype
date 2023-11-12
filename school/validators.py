from rest_framework import serializers


class EvenNumberValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if 'https://www.youtube.com/' not in tmp_val:
            raise serializers.ValidationError("The link must be only from youtube.")