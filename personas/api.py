from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Persona
from .serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    @action(detail=False, methods=['get'], url_path='buscar')
    def buscar_por_documento(self, request):
        numero_documento = request.data.get('numero_documento')

        if not numero_documento:
            return Response(
                {"error": "El número de documento es requerido"},
                status=status.HTTP_400_BAD_REQUEST
            )

        persona = Persona.objects.filter(numero_documento=str(numero_documento).strip()).first()

        if persona:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {"error": "Persona no encontrada"},
            status=status.HTTP_404_NOT_FOUND
        )