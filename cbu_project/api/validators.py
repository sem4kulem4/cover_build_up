from django.core.exceptions import ValidationError


def reach_validator(value):
    try:
        previous = value[0]
        for num, current in enumerate(value):
            if not 0 <= current <= 100:
                raise ValidationError('Numbers should be => 0, and <= 100')
            if previous < current:
                raise ValidationError('Numbers should go down')

            previous = current
    except ValueError:
        raise ValidationError('Incorrect values')
