from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.CharField(max_length=50, default='user')
    attributes = models.OneToOneField('Attributes', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'

    class Meta(AbstractUser.Meta):
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    attributes = models.OneToOneField('Attributes', on_delete=models.CASCADE)

    def __str__(self):
        return f'Задание {self.name}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Attributes(models.Model):
    KINDS = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    mathematics = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Математика')
    russian = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Руссский язык')
    literature = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Литература')
    history = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='История')
    music = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Музыка')
    chemistry = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Химия')
    biology = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Биология')
    physics = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Физика')
    ecology = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Экология')
    geography = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='География')
    astronomy = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Астрономия')
    technology = models.CharField(max_length=50, choices=KINDS, default='0', verbose_name='Технология')

    def __str__(self):
        return f'Id #{self.id}'

    class Meta:
        verbose_name = 'Атрибуты'
        verbose_name_plural = 'Атрибуты'


class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'Связь {self.user} - {self.task}'

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'
