from django.core.exceptions import ValidationError


def validate_username_me(username):
    if username == 'me':
        raise ValidationError('Нельзя использовать имя профиля me')
