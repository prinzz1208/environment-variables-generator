from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class GeneratorViewSet(ViewSet):
    def list(self, request):
        return Response("Initial setting")
