from django.db import models

class Task(models.Model):
    title = models.CharField('название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задача'

class Sem(models.Model):
    content = models.CharField('Введение', max_length=50)
    sem = models.TextField('Содержание')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name='Хай'
        verbose_name_plural='Хай'