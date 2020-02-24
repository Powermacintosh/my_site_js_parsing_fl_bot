from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from time import time

from django.shortcuts import reverse


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Fl(models.Model):
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    link = models.URLField(verbose_name='Ссылка на объявление', unique=True)
    show = models.TextField(verbose_name='Заголовок')
    price = models.TextField(verbose_name='Цена заказа', blank=True)
    ref_link = models.TextField(verbose_name='Объявление', null=True, blank=True)
    date_p = models.DateField(verbose_name='Дата публикации', blank=True)
    time_p = models.TextField(verbose_name='Время публикации', blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts_mtm')
    image = models.ImageField(blank=True, upload_to='images/')

    def get_absolute_url(self):
    	return reverse('fl_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('fl_update_url', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.show)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.show

    class Meta:
        ordering = ['-date_p', '-time_p']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)