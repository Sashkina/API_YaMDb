import csv
import logging
from django.core.management.base import BaseCommand
from reviews.models import Category, Genre, Title, Review, Comment
from users.models import User

# Настройка логгера
logging.basicConfig(filename='import.log', level=logging.INFO)

class Command(BaseCommand):
    help = "Наполняет базу данными из csv"

    def handle(self, *args, **options):
        # Запись информации о начале загрузки данных в лог
        logging.info('Начало загрузки данных')

        # Загрузка категорий
        with open("./static/data/category.csv", encoding='utf-8') as c_file:
            category_reader = csv.DictReader(c_file, delimiter=",")
            categories_to_create = []
            for row in category_reader:
                if Category.objects.filter(slug=row['slug']).exists():
                    self.stdout.write(
                        self.style.SUCCESS(
                            (f'{row["slug"]} уже существует, пропустим')
                        )
                    )
                    # Запись информации об успехе в лог
                    logging.info(f'{row["slug"]} уже существует, пропустим')
                else:
                    category = Category(
                        pk=row['id'],
                        name=row["name"],
                        slug=row["slug"]
                    )
                    categories_to_create.append(category)
                    self.stdout.write(
                        self.style.SUCCESS((
                            (f' Создана категория {row["slug"]} '
                             f'c id = {category.pk}'))
                        )
                    )
                    # Запись информации об успехе в лог
                    logging.info(f'Создана категория {row["slug"]} c id = {category.pk}')
            Category.objects.bulk_create(categories_to_create)

        # Загрузка жанров
        with open("./static/data/genre.csv", encoding='utf-8') as g_file:
            genre_reader = csv.DictReader(g_file, delimiter=",")
            genres_to_create = []
            for row in genre_reader:
                if Genre.objects.filter(slug=row['slug']).exists():
                    self.stdout.write(
                        self.style.SUCCESS(
                            (f'{row["slug"]} уже существует, пропустим')
                        )
                    )
                    # Запись информации об успехе в лог
                    logging.info(f'{row["slug"]} уже существует, пропустим')
                else:
                    genre = Genre(
                        pk=row['id'],
                        name=row["name"],
                        slug=row["slug"]
                    )
                    genres_to_create.append(genre)
                    self.stdout.write(
                        self.style.SUCCESS((
                            (f' Создан жанр {row["slug"]} '
                             f'c id = {genre.pk}'))
                        )
                    )
                    # Запись информации об успехе в лог
                    logging.info(f'Создан жанр {row["slug"]} c id = {genre.pk}')
            Genre.objects.bulk_create(genres_to_create)

        # Запись информации о завершении загрузки данных в лог
        logging.info('Загрузка данных завершена')
