from django.contrib import admin
from paciente.models import Paciente



class PacienteAdmin(admin.ModelAdmin):

    list_filter = ('nome','profissional')

    list_display = ('nome', 'sobrenome', 'data_nascimento','data_criacao','cpf','rg','profissional')

    search_fields = ('nome','sobrenome')

    fieldsets = (
        (None, {
            'fields': (('nome', 'sobrenome'), ('sexo','dt_nascimento'),'acompanhante',
                       ('cpf','rg'),'profissional')
        }),
        ('Endereco', {
            'fields': (('cep','endereco'),('complemento','bairro'),('cidade',
                     'uf'))
        }),
    )

admin.site.register(Paciente, PacienteAdmin)
admin.AdminSite.site_title = 'Sistema CRM '
admin.AdminSite.site_header = 'Administração'
admin.AdminSite.index_title = 'Painel'
