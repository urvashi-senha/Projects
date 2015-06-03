from pname.models import Word, Phoneme
from django import template

register = template.Library()


def audiofiles(string):
    s = ''
    if str(string) != 'None':
	s = '<audio controls="controls" controls="download"> <source src="' + str(string) + '" type="audio/mp3"></audio>'
    else:
	s = 'no file'
    return s


register.simple_tag(audiofiles)



