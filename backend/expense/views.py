from django.db.models import Q
from django.views.generic import ListView

from .models import Expense


class DatatablesMixin:
    paginate = 10
    rows_per_pages = (5, 10, 20, 50, 100)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rows_per_pages'] = self.rows_per_pages

        # Busca
        search = self.request.GET.get('search')
        if search:
            context['search'] = search

        # Ordenação
        sort_by = self.request.GET.get('sort_by')
        if sort_by:
            if '-' in sort_by:
                _sort_by = sort_by.replace('-', '')
                # key é o nome do campo a ser ordenado.
                key = _sort_by
            else:
                # Muda a ordenação (como se fosse toggle).
                _sort_by = f'-{sort_by}'
                key = sort_by
        else:
            # Pega o nome do primeiro campo de ordenação do model.
            key = self.model._meta.ordering[0].replace('-', '')
            _sort_by = key

        # Atualiza o dicionário procurando pelo campo de ordenação.
        self.sort_by[key]['ordering'] = _sort_by
        context['sort_by'] = self.sort_by
        context['ordering'] = _sort_by

        # Linhas por página
        rows_per_page = self.request.GET.get('rows_per_page')
        if rows_per_page:
            context['rows_per_page'] = rows_per_page
        else:
            context['rows_per_page'] = self.paginate

        # Total de itens
        total_items = self.model.objects.values_list('id', flat=True).count()
        context['total_items'] = total_items

        return context

    def get_paginate_by(self, queryset):
        rows_per_page = self.request.GET.get('rows_per_page')
        if rows_per_page:
            return rows_per_page
        return self.paginate


class ExpenseSearchMixin:
    '''
    Campo de busca
    '''

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            return queryset.filter(
                Q(description__icontains=search)
            )
        return queryset


class ExpenseSortMixin:
    '''
    Ordenação
    '''
    sort_by = {
        'pk': {
            'label': 'Descrição',
            'ordering': 'pk',
        },
        'description': {
            'label': 'Descrição',
            'ordering': 'description',
        },
        'payment_date': {
            'label': 'Data de pagamento',
            'ordering': 'payment_date',
        },
        'value': {
            'label': 'Valor',
            'ordering': 'value',
        },
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.sort_by
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by')

        if sort_by:
            return queryset.order_by(sort_by)
        return queryset


class ExpenseListView(DatatablesMixin, ExpenseSearchMixin, ExpenseSortMixin, ListView):
    model = Expense
    template_name = 'expense/expense_list.html'
