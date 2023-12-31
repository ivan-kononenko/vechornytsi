# Generated by Django 4.2.4 on 2023-09-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publication Date'),
        ),
    ]
