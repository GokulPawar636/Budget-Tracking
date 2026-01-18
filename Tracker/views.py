from django.shortcuts import render, redirect
from .models import CurrentBalance, TrackingHistory
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout as auth_logout,login as auth_login      
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('login')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

        # Login user
        auth_login(request, user)
        return redirect('index')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([username, first_name, last_name, password, confirm_password]):
            messages.error(request, 'All fields are required')
            return redirect('register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')

    return render(request, 'register.html')
@login_required(login_url='login')
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