from django import template
register = template.Library()

def flag(f):
    string = ''
    if f==0:
	    string =' <form action="fest2.html/" method="POST">'
    else:
	string = ' <form action="admin_fest2.html/" method="POST">'
    return string



    
register.simple_tag(flag)
