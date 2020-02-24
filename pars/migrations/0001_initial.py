# Generated by Django 2.2.7 on 2019-12-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('link', models.URLField(unique=True, verbose_name='Ссылка на объявление')),
                ('show', models.TextField(verbose_name='Заголовок')),
                ('price', models.TextField(blank=True, verbose_name='Цена')),
                ('ref_link', models.TextField(blank=True, null=True, verbose_name='Объявление')),
                ('date_p', models.DateField(blank=True, verbose_name='Дата публикации')),
                ('time_p', models.TextField(blank=True, verbose_name='Время публикации')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]