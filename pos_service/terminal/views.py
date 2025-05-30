from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
import requests

class TransactionView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                acquirer_response = requests.post(
                "http://acquirer:8001/process/",
                json=serializer.data,
                timeout=5
)
                return Response(acquirer_response.json(), status=acquirer_response.status_code)
            except requests.exceptions.RequestException as e:
                return Response({"error": "Acquirer unreachable"}, status=503)
        return Response(serializer.errors, status=400)