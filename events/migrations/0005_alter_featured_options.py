# Generated by Django 4.0.4 on 2022-05-26 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_review_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='featured',
            options={'verbose_name': 'Желаемое', 'verbose_name_plural': 'Список желаемого'},
        ),
    ]
