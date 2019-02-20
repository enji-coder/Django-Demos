from django import template

register=template.Library()



@register.filter(name='one_more')
def custom_filter(value_1):
    return value_1.upper()

register.filter('custom_filter', custom_filter)