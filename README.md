# api_yamdb

### Описание:

*Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории.
Произведению может быть присвоен жанр из списка предустановленных.
Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку;
из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.
Пользователи могут оставлять комментарии к отзывам.*


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Sashkina/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры:

1. **Получение списка всех отзывов**

**Request sample:**
GET api/v1/titles/{title_id}/reviews/

**Response sample:**
{
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
        + {...}
    ]
}

2. **Добавление комментария к отзыву**

**Request sample:**
POST api/v1/titles/{title_id}/reviews/{review_id}/comments/

{
    "text": "string"
}

**Response sample:**
{
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
}
