from django.db import models
from django.contrib.auth.models import User

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default = 0)

    def __str__(self) -> str:
        return f"The current balance is {self.current_balance}"
    


class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()

    expense_type = models.CharField(
        max_length=10,
        choices=[
            ('CREDIT', 'CREDIT'),
            ('DEBIT', 'DEBIT'),
        ]
    )

    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The amount is {self.amount} for {self.description} on {self.created_at} with {self.expense_type}"


class RequestLogs(models.Model):
    request_info = models.TextField()
    request_type = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):    
        return f"The request info is {self.request_info} for {self.request_type} on {self.created_at}"