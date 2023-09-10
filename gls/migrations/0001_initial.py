# Generated by Django 4.2 on 2023-06-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='Название')),
                ('start', models.CharField(max_length=45, verbose_name='Тираж')),
                ('desc', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
