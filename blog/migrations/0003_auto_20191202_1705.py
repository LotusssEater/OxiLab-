# Generated by Django 2.2.7 on 2019-12-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191106_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=450),
        ),
    ]
