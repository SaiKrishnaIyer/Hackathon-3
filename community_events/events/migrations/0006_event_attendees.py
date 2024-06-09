# Generated by Django 5.0.6 on 2024-06-09 03:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rename_rsvp_date_rsvp_timestamp_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='events_attending', to=settings.AUTH_USER_MODEL),
        ),
    ]
