from rest_framework.viewsets import ModelViewSet

from .models import Memo
from .serializers import MemoSerializer

import requests
import logging

logger = logging.getLogger(__name__)

class MemoAPIView(ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

    def get_queryset(self):
        return Memo.objects.all()

    def get_serializer_class(self):
        return MemoSerializer

    def get_serializer(self, *args, **kwargs):
        return MemoSerializer(*args, **kwargs)

    
    def list(self, request, *args, **kwargs):
        res = requests.get("https://naver.com")
        logger.info(f"Naver response: {res.status_code}")
        res = requests.get("http://192.168.71.74:8001/api/book/")
        logger.info(f"Book response: {res.status_code}")
        return super().list(request, *args, **kwargs)