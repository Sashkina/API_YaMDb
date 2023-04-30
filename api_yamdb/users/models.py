from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .utils import validate_username_me

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
ROLE_CHOICES = [
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор'),
]


class User(AbstractUser):
    username = models.TextField(
        'username',
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message='Неверно введено имя'
            ), validate_username_me]
    )

    email = models.EmailField(
        'email',
        unique=True,
        max_length=254,
        blank=False,
        null=False,
    )
    first_name = models.TextField(
        'name',
        blank=True,
        max_length=150
    )
    last_name = models.TextField(
        'last_name',
        blank=True,
        max_length=150
    )
    bio = models.TextField(
        'biography',
        blank=True,
        null=True,
        max_length=1000
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        default=USER,
        max_length=50
    )

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser
