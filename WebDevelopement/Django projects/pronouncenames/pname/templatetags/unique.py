from django import template
from pname.models import Word

register = template.Library()

def unique(list1):
    list2 = []
    for i in list1:
	if i.name not in list2:
	    list2.append(i.name)
    list2.sort()
    string = "<ul>"
#    for i in list2:
	#	string+= "<li>" +  str(i) + "/>" +  str(i) +"</a></li>"
#	string+= '<li> <form action="displayresult.html/" method="POST">{% csrf_token %}'  + str(i) + '<input type="hidden" name="word" id="word" value="' + str(i) + '"><input type="submit" value="Get Pronunciation"></form> </li>'
#    string += "</ul>"
    return list2
    
register.simple_tag(unique)


