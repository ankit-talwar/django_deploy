#custom template tag

from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value, arg):
    """
    cuts out all the value from arg from string
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, '')
# register.filter('cut',cut)