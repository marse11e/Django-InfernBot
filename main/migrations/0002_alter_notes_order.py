# Generated by Django 5.0 on 2023-12-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='order',
            field=models.IntegerField(default=0, help_text='Порядок сортировки заметок пользователя.', verbose_name='Порядок сортировки'),
        ),
    ]