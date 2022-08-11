from django.forms import Form, CharField

class Search(Form):
    nombre_producto = CharField(max_length=150)

