from haystack.indexes import *
from haystack import site
from models import Pagina 
import datetime

class PaginaIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='title')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Pagina.objects.filter(fecha__lte=datetime.datetime.now())

site.register(Pagina, PaginaIndex)
