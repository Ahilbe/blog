# Generated by Django 4.2 on 2024-04-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('goods', models.CharField(max_length=255)),
                ('vidio_devais', models.CharField(max_length=255)),
                ('npk', models.CharField(max_length=255)),
                ('phones', models.CharField(max_length=255)),
            ],
        ),
    ]
