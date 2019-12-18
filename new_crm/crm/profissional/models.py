from django.db import models


class Profissional(models.Model):

    ESPECIALIDADE = (
        ('f','Fonoaudiologo'),
        ('p','Psicologo'),
        ('n','Neurologista')
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

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )

    especialidade = models.CharField(
        'especialidade',
        max_length=1,
        choices=ESPECIALIDADE,
        default='f',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name_plural = 'profissionais' \
                              ''
    def __str__(self):
        return "{} {}".format(self.nome,self.sobrenome,self.especialidade)

    objetos = models.Manager()