# Generated by Django 4.0.4 on 2022-05-28 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_review_date_alter_review_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='events.events'),
        ),
    ]
