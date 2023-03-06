from django.db import models

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class TermoDeUsoEquipamento(Base):
    funcionario = models.CharField(max_length=100)
    nome_pc = models.CharField(max_length=50)
    ssd = models.CharField(max_length=50)
    memoria = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    monitor1 = models.CharField(max_length=50)
    monitor2 = models.CharField(max_length=50, blank=True)
    perifericos = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, blank=True, editable=False)
    observacao = models.TextField(blank=True)
    arquivo = models.FileField(upload_to='upload_to')

    def __str__(self):
        return self.funcionario
    
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.funcionario)

signals.pre_save.connect(produto_pre_save, sender=TermoDeUsoEquipamento)

