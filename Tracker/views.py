from django.shortcuts import render, redirect
from .models import CurrentBalance, TrackingHistory
from django.views.decorators.http import require_POST


def index(request):
    if request.method == 'POST' and request.POST.get('action') == 'add':
        description = request.POST.get("description")
        amount = float(request.POST.get("amount"))

        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)

        expense_type = 'DEBIT' if amount < 0 else 'CREDIT'

        TrackingHistory.objects.create(
            current_balance=current_balance,
            amount=amount,
            expense_type=expense_type,
            description=description
        )

        current_balance.current_balance += amount
        current_balance.save()

        return redirect('index')

    # FETCH DATA
    current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    transactions = TrackingHistory.objects.all().order_by('-created_at')

    income = sum(t.amount for t in transactions if t.amount > 0)
    expense = sum(abs(t.amount) for t in transactions if t.amount < 0)

    context = {
        'current_balance': current_balance,
        'income': income,
        'expense': expense,
        'transactions': transactions,
    }

    return render(request, 'index.html', context)

@require_POST
def delete_transaction(request, id):
    transaction = TrackingHistory.objects.get(id=id)
    current_balance = transaction.current_balance

    current_balance.current_balance -= transaction.amount
    current_balance.save()

    transaction.delete()
    return redirect('index')