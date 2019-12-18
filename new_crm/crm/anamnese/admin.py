from django.contrib import admin
from anamnese.models import Anamnese

class AnamneseAdmin(admin.ModelAdmin):

    list_filter = ('queixa','tempo_deficiencia')

    list_display = ('paciente', 'queixa')

    search_fields = ('queixa','tempo_deficiencia')

    fieldsets = (
        (None, {
            'fields': (('paciente', 'queixa'), ('tempo_deficiencia', 'causa'), 'historico_familiar')
        }),
        ('Dificuldades', {
            'fields': (('dif_tv', 'dif_ar'), ('dif_fone', 'dif_igreja'), ('dif_er', 'dif_trabalho'))
        }),
        ('Considerações Médicas', {
            'fields': (('zumbido','tipo_zumbido'),('infeccao','tipo_infeccao'),('cirurgia_ouvido','destreza_manual'),
                       ('problema_visual','protese_dentaria'),('medicamento','hipertensao'))
        }),
    )

    radio_fields = {'dif_tv':admin.HORIZONTAL,
                    'dif_fone':admin.HORIZONTAL,
                    'dif_er': admin.HORIZONTAL,
                    'dif_ar': admin.HORIZONTAL,
                    'dif_igreja': admin.HORIZONTAL,
                    'dif_trabalho':admin.HORIZONTAL}

    def upper_case_paciente(self,paciente):
        return ("%s" % (anamnese.paciente)).upper()
    upper_case_paciente.short_description = 'Nome do Paciente'

    def upper_case_queixa(self, queixa):
        return ("%s" % (anamnese.queixa)).upper()
    upper_case_queixa.short_description = 'Queixa principal'

admin.site.register(Anamnese,AnamneseAdmin)