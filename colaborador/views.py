from rest_framework import viewsets
from colaborador.models import Colaborador
from colaborador.serializers import ColaboradorSerializer


class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer