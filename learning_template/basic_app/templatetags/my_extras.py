from django import template

register = template.Library()
@registe.filter(name='cut')
def cut(value,arg):
    """
    This cuts off all the values of "arg" from string
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
