# Generated by Django 5.2 on 2025-04-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
    ]
