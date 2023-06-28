# Generated by Django 4.1.7 on 2023-06-11 20:03

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[1920, 1080], upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Article title'),
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(max_length=255, verbose_name='Event description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name='Event date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Event name'),
        ),
    ]
