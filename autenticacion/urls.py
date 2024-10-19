from django.urls import path

from .views import Vregistro


urlpatterns = [
    path('', Vregistro.as_view(), name="Autenticacion"),
]



