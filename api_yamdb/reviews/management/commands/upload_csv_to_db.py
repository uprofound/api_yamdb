import csv
import sqlite3

from django.core.management.base import BaseCommand

#TODO достать название БД из settings?

class Command(BaseCommand):
    help = 'TODO'

    file_name__table_name = {
        'users': 'users_user',
        'category': 'reviews_category',
        'genre': 'reviews_genre',
        'titles': 'reviews_title',
        'genre_title': 'reviews_title_genre',
        'review': 'reviews_review',
        'comments': 'reviews_comment',
    }

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='TODO')

    def upload_csv_to_db(self, file_name, table_name):
        try:
            #TODO обработчик пути к файлу для разных ОС?
            with open(f"static\data\{file_name}.csv", encoding="utf-8", newline="") as f, \
                    sqlite3.connect("db.sqlite3") as conn:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames
                fields = ','.join(fieldnames)
                values = ','.join(['?'] * len(fieldnames))
                data = [[row[fieldname] for fieldname in fieldnames] for row in reader]
                conn.executemany(f"INSERT INTO {table_name} ({fields}) VALUES ({values})", data)
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Во время загрузки данных в таблицу {table_name} '
                f'произошла ошибка:\n{e.__class__} - {e}\n\n')
            )
        else:
            self.stdout.write(self.style.SUCCESS(
                f'Данные в таблицу {table_name} успешно загружены!\n\n'
            ))

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']

        if file_name == 'all':
            for file_name, table_name in self.file_name__table_name.items():
                self.upload_csv_to_db(file_name, table_name)
        else:
            table_name = self.file_name__table_name.get(file_name)
            if table_name:
                self.upload_csv_to_db(file_name, table_name)
            else:
                self.stdout.write(self.style.ERROR('Запрошена загрузка неизветных данных'))
