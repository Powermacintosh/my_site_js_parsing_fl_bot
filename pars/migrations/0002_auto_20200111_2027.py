# Generated by Django 2.2.7 on 2020-01-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fl',
            options={'ordering': ['-date_p', '-time_p']},
        ),
        migrations.AlterField(
            model_name='fl',
            name='price',
            field=models.TextField(blank=True, verbose_name='Цена заказа'),
        ),
        migrations.AddField(
            model_name='fl',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts_mtm', to='pars.Tag'),
        ),
    ]
