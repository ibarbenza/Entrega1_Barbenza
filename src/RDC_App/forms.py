from django.forms import *

class Search(Form):
    nombre_producto = CharField(max_length=150)

class Form_Reseña(Form):
    titulo = CharField(max_length=50)
    contenido = CharField(max_length=2000)
    rating = IntegerField()
