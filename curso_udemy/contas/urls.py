from contas.views import Listagem,Nova_Transacao,Atualizar,Remover
from django.urls import path

app_name = 'contas'

urlpatterns = [
    # GET /
    path('', Listagem().as_view(), name="home"),

    # GET /funcionario/cadastrar
    path('transacao/url_nova', Nova_Transacao().as_view(), name="url_nova"),

    # GET/POST /funcionario/{pk}
    path('atualizar/<int:pk>', Atualizar().as_view(), name="url_atualizar"),

    # GET/POST /funcionarios/excluir/{pk}
    path('tramsacao/remover/<int:pk>', Remover().as_view(), name="url_remover"),
]