# Generated by Django 4.2.2 on 2023-06-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=25)),
                ('birthday', models.CharField(max_length=15)),
                ('age', models.CharField(max_length=3)),
                ('height', models.CharField(max_length=15)),
                ('weight', models.CharField(max_length=15)),
            ],
        ),
    ]
