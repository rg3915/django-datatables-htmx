from django import template

register = template.Library()


@register.simple_tag
def first_line_count(*args, **kwargs):
    '''
    Calcula o primeiro valor do número de linhas.
    '''
    pg_number = kwargs.get('pg_number')
    obj_count = kwargs.get('obj_count')
    return pg_number * obj_count - obj_count + 1


@register.simple_tag
def last_line_count(*args, **kwargs):
    '''
    Calcula o último valor do número de linhas.
    '''
    pg_number = kwargs.get('pg_number')
    obj_count = kwargs.get('obj_count')
    return pg_number * obj_count
