
from pname.models import Word, Phoneme
from django import template

register = template.Library()


def for_loop(list1):
    s = ''
    for i in list1:
	s += i
	s += '-'
    #a = word.split('-')
#	string = ''
#	for i in a:
#	    i = i.rstrip()
#	    i = i.lstrip()
#	    p = Phoneme.objects.get(phoneme=i)
#	    string += '<a href =' + '"' +  p.audiofile.url + '" target="blank">' + str(i) + '</a>-'

    return s[:-1]


register.simple_tag(for_loop)



