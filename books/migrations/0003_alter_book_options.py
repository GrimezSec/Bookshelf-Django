# Generated by Django 4.2.6 on 2024-02-26 07:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_book_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name": "Book", "verbose_name_plural": "Books"},
        ),
    ]
