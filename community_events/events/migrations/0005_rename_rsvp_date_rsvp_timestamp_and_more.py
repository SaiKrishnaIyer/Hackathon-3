# Generated by Django 5.0.6 on 2024-06-09 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_timestamp_rsvp_rsvp_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsvp',
            old_name='rsvp_date',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
        migrations.AddField(
            model_name='event',
            name='max_attendees',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
    ]
