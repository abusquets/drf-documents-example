from rest_framework import viewsets
# from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    lookup_field = 'title'
    parser_classes = (MultiPartParser,)
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
