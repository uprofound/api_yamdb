import csv
import os

from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class Command(BaseCommand):
    DATA_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../static/data/"))

    def import_user(self):
        file_name = 'users.csv'
        try:
            with open(Command.DATA_DIR + f"\\{file_name}", encoding="utf-8",
                      newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    User.objects.create(
                        pk=row['id'],
                        username=row['username'],
                        email=row['email'],
                        role=row['role'],
                        bio=row['bio'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                    )
        except Exception as e:
            self.stdout.write(f'Error to import: {e}')
        else:
            self.stdout.write(f'Data from {file_name} imported to db!')

    def import_title(self):
        file_name = 'titles.csv'
        try:
            with open(Command.DATA_DIR + f"\\{file_name}", encoding="utf-8",
                      newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    Title.objects.create(
                        pk=row['id'],
                        name=row['name'],
                        year=row['year'],
                        category=Category.objects.get(pk=row['category'])
                    )
        except Exception as e:
            self.stdout.write(f'Error to import: {e}')
        else:
            self.stdout.write(f'Data from {file_name} imported to db!')

    def import_genre_title(self):
        file_name = 'genre_title.csv'
        try:
            with open(Command.DATA_DIR + f"\\{file_name}", encoding="utf-8",
                      newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    title = Title.objects.get(
                        pk=row['title_id'],
                    )
                    title.genre.add(Genre.objects.get(pk=row['genre_id']))
                    title.save()
        except Exception as e:
            self.stdout.write(f'Error to import: {e}')
        else:
            self.stdout.write(f'Data from {file_name} imported to db!')

    def import_genre(self):
        file_name = 'genre.csv'
        try:
            with open(Command.DATA_DIR + f"\\{file_name}", encoding="utf-8",
                      newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    Genre.objects.create(
                        pk=row['id'],
                        name=row['name'],
                        slug=row['slug'],
                    )
        except Exception as e:
            self.stdout.write(f'Error to import: {e}')
        else:
            self.stdout.write(f'Data from {file_name} imported to db!')

    def import_category(self):
        file_name = 'category.csv'
        try:
            with open(Command.DATA_DIR + f"\\{file_name}", encoding="utf-8",
                      newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    Category.objects.create(
                        pk=row['id'],
                        name=row['name'],
                        slug=row['slug'],
                    )
        except Exception as e:
            self.stdout.write(f'Error to import: {e}')
        else:
            self.stdout.write(f'Data from {file_name} imported to db!')

    def import_review(self):
        file_name = 'review.csv'
        try:
            with open(Command.DATA_DIR + f"\\{file_name}", encoding="utf-8",
                      newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    Review.objects.create(
                        pk=row['id'],
                        title=Title.objects.get(pk=row['title_id']),
                        text=row['text'],
                        author=User.objects.get(pk=row['author']),
                        score=row['score'],
                        pub_date=row['pub_date'],
                    )
        except Exception as e:
            self.stdout.write(f'Error to import: {e}')
        else:
            self.stdout.write(f'Data from {file_name} imported to db!')

    def import_comments(self):
        file_name = 'comments.csv'
        try:
            with open(Command.DATA_DIR + f"\\{file_name}", encoding="utf-8",
                      newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    Comment.objects.create(
                        pk=row['id'],
                        review=Review.objects.get(pk=row['review_id']),
                        text=row['text'],
                        author=User.objects.get(pk=row['author']),
                        pub_date=row['pub_date'],
                    )
        except Exception as e:
            self.stdout.write(f'Error to import: {e}')
        else:
            self.stdout.write(f'Data from {file_name} imported to db!')

    def full_import(self):
        self.import_user()
        self.import_category()
        self.import_genre()
        self.import_title()
        self.import_genre_title()
        self.import_review()
        self.import_comments()

    def handle(self, *args, **kwargs):
        self.full_import()
