from django.db import models
from django.utils import timezone
from datetime import date
from profissional.models import Profissional


class Paciente(models.Model):
    PRONON_TRATAMENTO_CHOICES = (
        ('a', 'Arq.'),
        ('aa', 'Arqa.'),
        ('d', 'Dona'),
        ('dr', 'Dr.'),
        ('dra', 'Dra.'),
        ('e', 'Eng.'),
        ('ea', u'Engª.'),
        ('p', 'Prof.'),
        ('pa', 'Profa.'),
        ('sr', 'Sr.'),
        ('sra', 'Sra.'),
        ('srta', 'Srta.'),
    )

    SEXO_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    ESTADOS_CHOICES = (
        ('ac', 'Acre'),
        ('al', 'Alagoas'),
        ('ap', 'Amapá'),
        ('am', 'Amazonas'),
        ('ba', 'Bahia'),
        ('ce', 'Ceará'),
        ('df', 'Distrito Federal'),
        ('es', 'Espírito Santo'),
        ('go', 'Goiás'),
        ('ma', 'Maranhão'),
        ('mt', 'Mato Grosso'),
        ('ms', 'Mato Grosso do Sul'),
        ('mg', 'Minas Gerais'),
        ('pa', 'Pará'),
        ('pb', 'Paraíba'),
        ('pr', 'Paraná'),
        ('pe', 'Pernambuco'),
        ('pi', 'Piauí'),
        ('rj', 'Rio de Janeiro'),
        ('rn', 'Rio Grande do Norte'),
        ('rs', 'Rio Grande do Sul'),
        ('ro', 'Rondônia'),
        ('rr', 'Roraima'),
        ('sc', 'Santa Catarina'),
        ('sp', 'São Paulo'),
        ('se', 'Sergipe'),
        ('to', 'Tocantins')
    )
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    tratamento = models.CharField(
        'tratamento',
        max_length=4,
        choices=PRONON_TRATAMENTO_CHOICES,
        null=True,
        blank=True
    )

    dt_nascimento = models.DateField(
        'data nascimento',
        null=True,
        blank=True
    )

    dt_criacao = models.DateField(
        'criado em',
        null=True,
        blank=True,
        auto_now_add=True,
        auto_now=False
    )

    dt_alteacao = models.DateField(
        'modificado em',
        null=True,
        blank=True,
        auto_now_add=False,
        auto_now=True
    )

    acompanhante = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        null=True,
        blank=True
    )
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        null=True,
        blank=True
    )
    rg = models.CharField(
        'RG',
        max_length=11,
        null=True,
        blank=True
    )

    profissional = models.ForeignKey(
        Profissional,
        max_length=100,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    active = models.BooleanField(
        'Ativo',
        default=True
    )

    blocked = models.BooleanField(
        'Bloqueado',
        default=False
    )

    endereco = models.CharField(
        'endereço',
        max_length=100,
        blank=True
    )

    complemento = models.CharField(
        'complemento',
        max_length=100,
        blank=True
    )

    bairro = models.CharField(
        'bairro',
        max_length=100,
        blank=True
    )

    cidade = models.CharField(
        'cidade',
        max_length=100,
        blank=True
    )

    cep = models.CharField(
        'CEP',
        max_length=9,
        blank=True
    )

    uf = models.CharField(
        'UF', max_length=2,
        choices=ESTADOS_CHOICES,
        blank=True
    )

    @property
    def data_nascimento(self):
        return self.dt_nascimento.strftime('%d/%m/%Y')

    @property
    def data_criacao(self):
        return self.dt_criacao.strftime('%d/%m/%Y')

    def __str__(self):
        return self.nome

objetos = models.Manager()
