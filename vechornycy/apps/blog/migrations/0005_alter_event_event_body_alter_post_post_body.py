# Generated by Django 4.2.4 on 2023-08-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_event_event_body_alter_post_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_body',
            field=models.TextField(),
        ),
    ]