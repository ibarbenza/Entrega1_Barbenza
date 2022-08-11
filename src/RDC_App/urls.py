from django.urls import path
from RDC_App.views import *

urlpatterns = [
    path("inicio/", index, name="index"),
    path("reseña", reseña, name="reseña")
]
