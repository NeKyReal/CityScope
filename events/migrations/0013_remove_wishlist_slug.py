# Generated by Django 4.0.4 on 2022-05-28 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_alter_wishlist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='slug',
        ),
    ]