from django.urls import path

from backend.expense import views as v

app_name = 'expense'


urlpatterns = [
    path('', v.ExpenseListView.as_view(), name='expense_list'),
]
