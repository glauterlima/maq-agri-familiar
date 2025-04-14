from django.urls import path
from lacunatecnologica.views import index

urlpatterns = [
    path('', index)
]
