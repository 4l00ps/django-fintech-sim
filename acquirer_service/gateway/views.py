from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
import logging

logger = logging.getLogger(__name__)


class ProcessTransactionView(APIView):
    def post(self, request):
        logger.debug(f"Received data: {request.data}")
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"status": "forwarded to switch (mock)"}, status=200)
        return Response(serializer.errors, status=400)
