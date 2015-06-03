from django import template
from pname.models import Word,RequestWord
register = template.Library()

def req(rec,words):
    string = ''

    for r in rec :
	flag = 0;
	for w in words:
	 if r.word == w.name:
	     flag = 1;
	     break;
	if flag==0:
	    string += "<li>" + r.word + "</li>"
    string +="</ol>"
    return string



    
register.simple_tag(req)
