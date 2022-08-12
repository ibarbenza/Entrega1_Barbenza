from django.urls import path
from RDC_App.views import *

urlpatterns = [
    path("inicio/", index, name="index"),
    path("reseña/", reseña, name="reseña"),
    path("add", add_reseña, name="add_reseña"),
    path("bebidas/", bebidas, name='bebidas'),
    path("copas", copas, name="copas")
]
