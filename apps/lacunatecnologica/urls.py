from django.urls import path
from apps.lacunatecnologica.views import index

urlpatterns = [
    path('', index)
]
