from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

from .validators import reach_validator

User = get_user_model()


class Curve(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь, к которому привязана кривая'
    )
    unit = models.PositiveIntegerField()
    reach = ArrayField(
        base_field=models.FloatField(), size=10, validators=[reach_validator]
    )

    def __str__(self):
        return f'{self.unit} ### {self.reach}'
