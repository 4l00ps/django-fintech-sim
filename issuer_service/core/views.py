from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuthorizeView(APIView):
    def post(self, request):
        card_number = request.data.get("card_number")
        amount = float(request.data.get("amount", 0))

        if not card_number or len(card_number) != 16:
            return Response({"response_code": "14", "message": "Invalid card"}, status=400)

        if amount > 1000:  # Mock rule: decline anything over 1000
            return Response({"response_code": "51", "message": "Insufficient funds"}, status=402)

        return Response({"response_code": "00", "message": "Approved"}, status=200)