from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer

import requests
import logging

logger = logging.getLogger(__name__)

class BookAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer

    def get_serializer(self, *args, **kwargs):
        return BookSerializer(*args, **kwargs)

    
    def list(self, request, *args, **kwargs):
        res = requests.get("https://kakao.com")
        logger.info(f"Kakao response: {res.status_code}")
        return super().list(request, *args, **kwargs)