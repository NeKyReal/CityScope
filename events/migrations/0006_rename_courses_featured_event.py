# Generated by Django 4.0.4 on 2022-05-27 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_featured_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featured',
            old_name='courses',
            new_name='event',
        ),
    ]
