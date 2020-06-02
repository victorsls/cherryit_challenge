from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Meeting(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Criando em'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Atualizado em'), auto_now=True)
    title = models.CharField(verbose_name=_('Titulo'), max_length=255)
    purpose = models.CharField(verbose_name=_('Motivo'), max_length=255)
    date = models.DateTimeField(verbose_name=_('Data'))
    image = models.ImageField(verbose_name=_('Imagem'), upload_to='meeting/images')
    employees = models.ManyToManyField(User, verbose_name=_('Funcionários'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Reunião')
        verbose_name_plural = _('Reuniões')
