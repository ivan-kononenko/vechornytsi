# Generated by Django 4.2.4 on 2023-09-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
