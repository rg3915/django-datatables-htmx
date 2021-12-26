from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.pop('rows_per_page', None)
    query.pop('page', None)
    query.pop('search', None)
    query.pop('sort_by', None)
    query.update(kwargs)
    return query.urlencode()
