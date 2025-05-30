from django.urls import path
from .views import ProcessTransactionView

urlpatterns = [
    path('process/', ProcessTransactionView.as_view(), name='process-transaction'),
]