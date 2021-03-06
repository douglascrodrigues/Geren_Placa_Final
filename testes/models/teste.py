from django.db import models
from django.db.models import constraints
from placas.models import modelo_placas, cadastro_lote
from contas.models import Usuario


STATUS_CHOICES = (  
    ("Pendente", "Pendente"),
    ("Em andamento", "Em andamento"), 
    ("Finalizado", "Finalizado")
)

SITUACAO_CHOICES = (  
    ("Aprovado","Aprovado"),
    ("Reprovado","Reprovado")
)

ETAPA_CHOICES = (
    ("Pendente", "Pendente"), 
    ("Burn In","Burn In"),
    ("Pre-Teste","Pre-Teste"),
    ("Teste Final","Teste Final")
)

class Teste(models.Model):
    Etapa_teste = models.CharField(
        'Etapa do teste',
        choices=ETAPA_CHOICES,
        max_length = 20
    )
    
    Item_requisicao = models.ForeignKey(
        'requisicao.item_requisicao',
        on_delete=models.CASCADE,
        related_name='Requisicao_Item_Requisicao',
        blank = True
    )

    Lote_numero = models.CharField(
        'Número de Lote',
        max_length=50,
        blank = True,
        null=True
    )
    
    Data_teste = models.DateTimeField(
        'Data Início',
        auto_now=True,
        blank = True
    )
    
    Fim = models.DateTimeField(
        'Data Fim',
        blank = True,
        null = True
    )

    Status = models.CharField(
        'Status do Teste',
        choices=STATUS_CHOICES,
        max_length = 20,
        blank=True
    )

    Situacao = models.CharField(
        'Situação do teste',
        choices=SITUACAO_CHOICES,
        max_length = 20
    ) 

    Observacao = models.CharField(
        'Observação', 
        max_length=100
    )

    username = models.ForeignKey(
        'contas.usuario',
        related_name='contas_usuario_username_teste',
        on_delete = models.PROTECT,
        editable = False,
        default = ""
    )

    def __str__(self):
        return self.Etapa_teste

    class Meta:
        db_table = 'CADASTRO_TESTE'