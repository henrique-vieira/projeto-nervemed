from django.contrib.admin import forms
from django.db import models
from django.forms import RadioSelect
from multiselectfield import MultiSelectField
from paciente.models import Paciente
from select_multiple_field.widgets import SelectMultipleField


class Anamnese(models.Model):

    # DIFICULDADE_CHOICES = (
    #     ('v','TV'),
    #     ('f','Telefone'),
    #     ('e','Encontros e Reuniões'),
    #     ('r','Ambientes Ruidosos'),
    #     ('i','Igrejas'),
    #     ('t','Trabalho')
    # )
    DIF_TV_CHOICES = (
        ('s','SIM'),
        ('n','NAO')
    )
    DIF_FONE_CHOICES = (
        ('s', 'SIM'),
        ('n', 'NAO')
    )
    DIF_ER_CHOICES = (
        ('s', 'SIM'),
        ('n', 'NAO')
    )
    DIF_AR_CHOICES = (
        ('s', 'SIM'),
        ('n', 'NAO')
    )
    DIF_IGREJA_CHOICES = (
        ('s', 'SIM'),
        ('n', 'NAO')
    )
    DIF_TRABALHO_CHOICES = (
        ('s', 'SIM'),
        ('n', 'NAO')
    )

    paciente = models.ForeignKey(
        Paciente,
        max_length=100,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    queixa = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    tempo_deficiencia = models.IntegerField(
        blank=True,
        null=True
    )

    causa = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    historico_familiar = models.TextField (
        blank=True,
        null=True
    )

    dif_tv = models.CharField (
        'TV',
        choices=DIF_TV_CHOICES,
        max_length=1,
        default='n'

    )
    dif_fone = models.CharField(
        'Telefone',
        choices=DIF_FONE_CHOICES,
        max_length=1,
        default = 'n'

    )
    dif_er = models.CharField(
        'Encontros e Reuniões',
        choices=DIF_ER_CHOICES,
        max_length=1,
        default='n'

    )
    dif_ar = models.CharField(
       'Ambientes Ruidosos',
       choices=DIF_AR_CHOICES,
        max_length=1,
        default='n'

    )
    dif_igreja = models.CharField(
        'Igrejas',
        choices=DIF_IGREJA_CHOICES,
        max_length=1,
        default='n'

    )
    dif_trabalho = models.CharField(
        'Trabalho',
        choices=DIF_TRABALHO_CHOICES,
        max_length=1,
        default='n'
    )

    zumbido = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    tipo_zumbido = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    infeccao = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    tipo_infeccao = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    cirurgia_ouvido = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    destreza_manual = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    problema_visual = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    protese_dentaria = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    medicamento = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    hipertensao = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.queixa


objetos = models.Manager()



