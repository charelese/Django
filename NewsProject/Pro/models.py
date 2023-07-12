from django.db import models
from django.urls import reverse_lazy

class Human(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя')
    surname = models.CharField(max_length=25, verbose_name='Фамилия')
    birthday = models.CharField(max_length=15, verbose_name='День рождения')
    age = models.CharField(max_length=3, verbose_name='Возраст')
    height = models.CharField(max_length=15, verbose_name='Рост')
    weight = models.CharField(max_length=15, verbose_name='Вес')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')


    def get_absolute_url(self):
        return reverse_lazy('View_human', kwargs={'pk': self.pk})

    class Meta:
        verbose_name='Человек'
        verbose_name_plural='Люди'
        ordering = ['name']

class Profession(models.Model):
    name = models.CharField(max_length=80, db_index=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('Profession', kwargs={'profession_id': self.pk})

    class Meta:
         verbose_name='Профессия'
         verbose_name_plural ='Профессии'
         ordering = ['name']
