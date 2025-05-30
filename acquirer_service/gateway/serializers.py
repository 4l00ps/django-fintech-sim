from rest_framework import serializers

class TransactionSerializer(serializers.Serializer):
    terminal_id = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    card_number = serializers.CharField()
    expiry_date = serializers.CharField()
    cvv = serializers.CharField()