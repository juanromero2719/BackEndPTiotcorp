from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    @action(detail=False, methods=['get'], url_path='buscar-por-fecha-limite')
    def buscar_por_fecha_limite(self, request):

        fecha_limite = request.data.get('fecha_limite')

        print(fecha_limite)
        if not fecha_limite:
            return Response(
                {"error": "Debes proporcionar el parámetro 'fecha_limite'."},
                status=400
            )

        queryset = self.get_queryset().filter(fecha_limite=fecha_limite)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='buscar-por-rango-fecha')
    def buscar_por_rango_fecha(self, request):

        fecha_limite_min = request.data.get('fecha_limite_min')
        fecha_limite_max = request.data.get('fecha_limite_max')

        if not fecha_limite_min or not fecha_limite_max:
            return Response(
                {"error": "Debes proporcionar los parámetros 'fecha_limite_min' y 'fecha_limite_max'."},
                status=400
            )

        queryset = self.get_queryset().filter(
            fecha_limite__range=[fecha_limite_min, fecha_limite_max]
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='buscar-por-persona')
    def buscar_por_persona(self, request):

        tipo_documento = request.data.get('tipo_documento')
        numero_documento = request.data.get('numero_documento')

        queryset = self.get_queryset()

        if tipo_documento:
            queryset = queryset.filter(persona__tipo_documento=tipo_documento)
        if numero_documento:
            queryset = queryset.filter(persona__numero_documento=numero_documento)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    