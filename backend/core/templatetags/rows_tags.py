from django import template

register = template.Library()


@register.simple_tag
def first_line_count(*args, **kwargs):
    '''
    Calcula o primeiro valor do número de linhas.
    '''
    pg_number = kwargs.get('pg_number')
    rows_per_page = int(kwargs.get('rows_per_page'))
    return pg_number * rows_per_page - rows_per_page + 1


@register.simple_tag
def last_line_count(*args, **kwargs):
    '''
    Calcula o último valor do número de linhas.
    '''
    pg_number = kwargs.get('pg_number')
    rows_per_page = int(kwargs.get('rows_per_page'))
    total_items = kwargs.get('total_items')

    last_line_count = pg_number * rows_per_page

    if total_items < last_line_count:
        return total_items
    return last_line_count
