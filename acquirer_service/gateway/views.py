import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer

logger = logging.getLogger(__name__)  # Setup logger

class ProcessTransactionView(APIView):
    def post(self, request):
        logger.debug(f"Incoming transaction data: {request.data}")  # Log request data

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            logger.debug("Transaction data is valid.")
            return Response({"status": "forwarded to switch (mock)"}, status=200)

        logger.debug(f"Validation errors: {serializer.errors}")  # Log validation errors
        return Response(serializer.errors, status=400)