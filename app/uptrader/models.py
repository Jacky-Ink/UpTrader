from django.db import models


class Mainmenu(models.Model):
    name = models.CharField(
        'Название',
        max_length=100
        )
    slug = models.SlugField(
        null=False,
        unique=True
        )
    position = models.PositiveIntegerField(
        'Позиция',
        default=1
        )
    parent = models.CharField(
        'parent',
        max_length=100,
        default=None,
        null=True
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
