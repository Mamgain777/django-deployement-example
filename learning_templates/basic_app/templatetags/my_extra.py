from atexit import register
from django import template

register = template.Library()

@register.filter(name='add')
def add(value,arg=20):
    """
    ADD WORLD TO HELLO
    """
    
    return value.replace(value,(value+arg))