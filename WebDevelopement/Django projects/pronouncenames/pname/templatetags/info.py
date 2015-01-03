from pname.models import Word, Phoneme
from django import template

register = template.Library()


def info(string):
    s = ''
    if str(string) != 'None':
	s = str(string) 
    return s


register.simple_tag(info)



