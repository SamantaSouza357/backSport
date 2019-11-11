from rest_framework import viewsets
from eventos.models import Eventos
from eventos.serializers import EventosSerializer


class EventosViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer