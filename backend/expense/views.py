from django.db.models import Q
from django.views.generic import ListView

from .models import Expense


class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expense_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rows_per_pages'] = (5, 10, 20, 50, 100)

        search = self.request.GET.get('search')
        if search:
            context['search'] = search

        rows_per_page = self.request.GET.get('rows_per_page')
        if rows_per_page:
            context['rows_per_page'] = rows_per_page
        else:
            context['rows_per_page'] = 10

        return context

    def get_paginate_by(self, queryset):
        rows_per_page = self.request.GET.get('rows_per_page')
        if rows_per_page:
            return rows_per_page
        return 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            return queryset.filter(
                Q(description__icontains=search)
            )
        return queryset
