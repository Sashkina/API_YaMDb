import csv

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from reviews.models import (Category, Genre, Title,
                            Review, Comment, TitleGenreAssign)
from users.models import User

class Command(BaseCommand):
    help = 'Импорт данных из CSV-файла'

    def handle(self, *args, **options):
        with open('./static/data/category.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    Category.objects.create(
                        id=row['id'],
                        name=row['name'],
                        slug=row['slug']
                    )
                except IntegrityError as e:
                    print(f"Error processing row: {row}, {e}")
                    pass

        with open('./static/data/genre.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    Genre.objects.create(
                        id=row['id'],
                        name=row['name'],
                        slug=row['slug']
                    )
                except IntegrityError as e:
                    print(f"Error processing row: {row}, {e}")
                    pass

        with open('./static/data/titles.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = Category.objects.get(id=row['category'])
                try:
                    Title.objects.create(
                        id=row['id'],
                        name=row['name'],
                        year=row['year'],
                        category=category
                    )
                except IntegrityError as e:
                    print(f"Error processing row: {row}, {e}")
                    pass

        with open('./static/data/genre_title.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = Title.objects.get(id=row['title_id'])
                genre = Genre.objects.get(id=row['genre_id'])
                try:
                    TitleGenreAssign.objects.create(
                        title=title,
                        genre=genre
                    )
                except IntegrityError as e:
                    print(f"Error processing row: {row}, {e}")
                    pass

        with open('./static/data/users.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    User.objects.create(
                        username=row['username'],
                        email=row['email'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        bio=row['bio'],
                        role=row['role']
                    )
                except IntegrityError as e:
                    print(f"Error processing row: {row}, {e}")
                    pass
   
        with open('./static/data/review.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User.objects.get(id=row['author'])
                title = Title.objects.get(id=row['title'])
                try:
                    Review.objects.create(
                        author=user,
                        text=row['text'],
                        score=row['score'],
                        title=title
                    )
                except IntegrityError as e:
                    print(f"Error processing row: {row}, {e}")
                    pass

        with open('./static/data/comments.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User.objects.get(id=row['author'])
                review = Review.objects.get(id=row['review'])
                try:
                    Comment.objects.create(
                        author=user,
                        review=review,
                        text=row['text']
                    )
                except IntegrityError as e:
                    print(f"Error processing row: {row}, {e}")
                    pass

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))




























# import csv
# import logging

# from django.core.management.base import BaseCommand
# from reviews.models import Category, Genre

# # Настройка логгера
# logging.basicConfig(filename='import.log', level=logging.INFO)


# class Command(BaseCommand):
#     help = "Наполняет базу данными из csv"

#     def handle(self, *args, **options):
#         # Запись информации о начале загрузки данных в лог
#         logging.info('Начало загрузки данных')

#         # Загрузка категорий
#         with open("./static/data/category.csv", encoding='utf-8') as c_file:
#             category_reader = csv.DictReader(c_file, delimiter=",")
#             categories_to_create = []
#             for row in category_reader:
#                 if Category.objects.filter(slug=row['slug']).exists():
#                     self.stdout.write(
#                         self.style.SUCCESS(
#                             (f'{row["slug"]} уже существует, пропустим')
#                         )
#                     )
#                     # Запись информации об успехе в лог
#                     logging.info(f'{row["slug"]} уже существует, пропустим')
#                 else:
#                     category = Category(
#                         pk=row['id'],
#                         name=row["name"],
#                         slug=row["slug"]
#                     )
#                     categories_to_create.append(category)
#                     self.stdout.write(
#                         self.style.SUCCESS((
#                             (f' Создана категория {row["slug"]} '
#                              f'c id = {category.pk}'))
#                         )
#                     )
#                     # Запись информации об успехе в лог
#                     logging.info(f'Создана категория {row["slug"]}'
#                                  f'c id = {category.pk}'
#                                  )
#             Category.objects.bulk_create(categories_to_create)

#         # Загрузка жанров
#         with open("./static/data/genre.csv", encoding='utf-8') as g_file:
#             genre_reader = csv.DictReader(g_file, delimiter=",")
#             genres_to_create = []
#             for row in genre_reader:
#                 if Genre.objects.filter(slug=row['slug']).exists():
#                     self.stdout.write(
#                         self.style.SUCCESS(
#                             (f'{row["slug"]} уже существует, пропустим')
#                         )
#                     )
#                     # Запись информации об успехе в лог
#                     logging.info(f'{row["slug"]} уже существует, пропустим')
#                 else:
#                     genre = Genre(
#                         pk=row['id'],
#                         name=row["name"],
#                         slug=row["slug"]
#                     )
#                     genres_to_create.append(genre)
#                     self.stdout.write(
#                         self.style.SUCCESS((
#                             (f' Создан жанр {row["slug"]} '
#                              f'c id = {genre.pk}'))
#                         )
#                     )
#                     # Запись информации об успехе в лог
#                     logging.info(f'Создан жанр {row["slug"]}'
#                                  f'c id = {genre.pk}'
#                                  )
#             Genre.objects.bulk_create(genres_to_create)

#         # Запись информации о завершении загрузки данных в лог
#         logging.info('Загрузка данных завершена')
