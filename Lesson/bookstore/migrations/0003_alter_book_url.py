# Generated by Django 5.1.2 on 2024-10-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_book_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
