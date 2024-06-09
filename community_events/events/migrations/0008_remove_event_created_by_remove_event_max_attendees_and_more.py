# Generated by Django 5.0.6 on 2024-06-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_event_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='event',
            name='max_attendees',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.RemoveField(
            model_name='review',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Default Event Name', max_length=255),
        ),
        migrations.AddField(
            model_name='review',
            name='user_name',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='user_name',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]