# Generated by Django 4.2.4 on 2023-09-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publication Date'),
        ),
    ]
