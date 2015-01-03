from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Word,Phoneme,RequestWord,WordKey
from forms import WordForm,RequestWordForm
from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login,logout
from django.utils.datastructures import MultiValueDictKeyError
from ctypes import *
import random
import string
import datetime
import os
import subprocess
# Create your views here.

def home(request):
    record = RequestWord.objects.all()
    words = Word.objects.all()
    context = RequestContext(request, { 'record' : record,'words':words } )
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context))


def namelist(request):
    context = RequestContext(request)
    template = loader.get_template('names_list.html')
    return HttpResponse(template.render(context))


def tempor(request):
   if request.method=='POST':
     if request.POST.get('s')!= 'None':
      word = request.POST.get('s')
      context = RequestContext(request, { 'w':word })
      template = loader.get_template('temp.html')
      return HttpResponse(template.render(context))


def search(request):
   if request.method=='POST':
     if request.POST.get('s')!= 'None':
      word = request.POST.get('s')
      if word:
       record = Word.objects.filter(name__startswith=word).order_by('-votes')
       if request.user.is_authenticated() :
       	template = loader.get_template('search.html')
       else:
       	template = loader.get_template('search.html')
       list1= []
       if len(record)>0:
        for i in record:
	 a = Word()
	 a.pk = i.pk
	 a.name = i.name
	 a.phomene = i.phomene
	 if i.audiofile=='':
	    a.audiofile = 'None'
	 else:
	    a.audiofile= i.audiofile
	 if i.pos=='':
	    a.pos = 'None'
	 else:
	    a.pos= i.pos
	 if i.origin=='':
	    a.origin = 'None'
	 else:
	    a.origin= i.origin
	 if i.meaning=='':
	    a.meaning = 'None'
	 else:
	    a.meaning= i.meaning
	 list1.append(a)
	context = RequestContext(request, { 'record' : list1,'w':word } )
        return HttpResponse(template.render(context))
       else:
        try:
         null = open("/dev/null","w")
         subprocess.Popen("festival",stdout=null,stderr=null)
	 message = 'Sorry, No results. See suggested pronounciation and add if correct.' 
	 string = "festival -b '(print (lex.lookup " +  '"' + str(word) +'"' + "))'> temp.txt"
	 os.system(string)
	 f = open('temp.txt','r')
	 text = f.readlines()
	 l = []
	 a = text[0][:-1]
	 b = a.split()
	 c = b[2:]
	 d = c[0].split('(((')
	 for i in d :
	    i = i.lstrip('(').rstrip(')')
	    l.append(i)
	 j = (c[1:-2])
	 for i in j:
	    i = i.lstrip('(').rstrip(')')
	    l.append(i)
	 f = c[-2].split(')')
	 l.append(f[0].lstrip('(').rstrip(')'))
	 e = c[-1].split(')))')
	 for i in e:
	     i = i.lstrip('(').rstrip(')')
	     l.append(i)
	 m = []
	 for i in l:
	     if str(i).isalpha():
		   m.append(i)
        except OSError:
	    message = ""
	    m = "[]"
	context = RequestContext(request,{'m': m,'w':word,'message':message})
        if request.user.is_authenticated() :
       	 template = loader.get_template('search.html')
        else:
         template = loader.get_template('search.html')
        return HttpResponse(template.render(context))

     if request.POST.get('word2')!=None:
        word = request.POST['word2']
	w = Word.objects.get(pk=request.POST['word2'])
	w.votes-=1
	w.save()
        record = Word.objects.filter(name__startswith=w.name).order_by('-votes')
        list1= []
        for i in record:
	 a = Word()
	 a.pk = i.pk
	 a.name = i.name
	 a.phomene = i.phomene
	 if i.audiofile=='':
	    a.audiofile = 'None'
	 else:
	    a.audiofile= i.audiofile
	 if i.pos=='':
	    a.pos = 'None'
	 else:
	    a.pos= i.pos
	 if i.origin=='':
	    a.origin = 'None'
	 else:
	    a.origin= i.origin
	 if i.meaning=='':
	    a.meaning = 'None'
	 else:
	    a.meaning= i.meaning
	 list1.append(a)
        if request.user.is_authenticated() :
       	 template = loader.get_template('search.html')
        else:
         template = loader.get_template('search.html')
	context = RequestContext(request, { 'record' : list1,'message':'Result voted down !!' } )
        return HttpResponse(template.render(context))
     if request.POST.get('word1')!=None:
        word = request.POST['word1']
	w = Word.objects.get(pk=request.POST['word1'])
	w.votes+=1
	w.save()
        record = Word.objects.filter(name__startswith=w.name).order_by('-votes')
	list1= []
        for i in record:
	 a = Word()
	 a.pk = i.pk
	 a.name = i.name
	 a.phomene = i.phomene
	 if i.audiofile=='':
	    a.audiofile = 'None'
	 else:
	    a.audiofile= i.audiofile
	 if i.pos=='':
	    a.pos = 'None'
	 else:
	    a.pos= i.pos
	 if i.origin=='':
	    a.origin = 'None'
	 else:
	    a.origin= i.origin
	 if i.meaning=='':
	    a.meaning = 'None'
	 else:
	    a.meaning= i.meaning
	 list1.append(a)
        if request.user.is_authenticated() :
       	 template = loader.get_template('search.html')
        else:
         template = loader.get_template('search.html')
	context = RequestContext(request, { 'record' : list1,'message' : 'Result voted up !!' } )
        return HttpResponse(template.render(context))
   else:    
     context = RequestContext(request)
     if request.user.is_authenticated() :
       	template = loader.get_template('search.html')
     else:
     	template = loader.get_template('search.html')
     return HttpResponse(template.render(context))
   


def addword2(request):
    template = loader.get_template('addword2.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def addword3(request):
    if request.method=='POST':
     w = request.POST['w']
     try:
	message = ''
        null = open("/dev/null","w")
        subprocess.Popen("festival",stdout=null,stderr=null)
        string = "festival -b '(print (lex.lookup " +  '"' + str(w) +'"' + "))'> temp.txt"
	null.close()
	os.system(string)
	f = open('temp.txt','r')
	text = f.readlines()
	l = []
	a = text[0][:-1]
	b = a.split()
	c = b[2:]
	d = c[0].split('(((')
	for i in d :
	    i = i.lstrip('(').rstrip(')')
	    l.append(i)
	j = (c[1:-2])
	for i in j:
	    i = i.lstrip('(').rstrip(')')
	    l.append(i)
	f = c[-2].split(')')
	l.append(f[0].lstrip('(').rstrip(')'))
	e = c[-1].split(')))')
	for i in e:
	     i = i.lstrip('(').rstrip(')')
	     l.append(i)
	m = []
	for i in l:
	     if str(i).isalpha():
		   m.append(i)
     except OSError:
	 m = "[]"
	 message = ""

     context = RequestContext(request,{'m': m,'w':w,'message':message})
     if request.user.is_authenticated() :
    		template = loader.get_template('addword3.html')
     else:
    		template = loader.get_template('addword3.html')
     return HttpResponse(template.render(context))

def addword4(request):
    if request.method=='POST':
	w = request.POST['w']
	M = str(request.POST['m'])
	newword = Word()
	if request.POST['m2']!='':
		m = request.POST['m2']
	  	phons = ['','aa','ae','ah','ao','aw','ax','ay','eh','el','em','en','er','ey','ih','iy','ow','oy','uh','uw','b','ch','d','dh','f','g','hh','jh','k','l','m','n','ng','p','r','s','sh','t','th','v','w','y','z','zh']
		#phons = [ 'I' ,'I' ,'e','E', '{', 'y' ,'2', '9', '1', '@', '6', '3', 'a', '}', '8', '&', 'M', '7', 'V', 'A' ,'u', 'U', 'o', 'O', 'Q' ,'p', 'b', 't', 'd', 'ts', 'dz', 'tS', 'dZ', 'c', 'J\\', 'k', 'g', 'q', 'p\\', 'B', 'f', 'v', 'T' ,'D', 's', 'z', 'Z', 'S', 'C', 'j\\', 'x', 'G', 'X\\', '?\\', 'h', 'h\\', 'm', 'F', 'n', 'J', 'N', 'l', 'L', '5', '4', 'r', 'r\\', 'R', 'P', 'w', 'H', 'j' ]
		m = m.split(',')
		p = ''
		for i in m:
		    i = i.lstrip('[').rstrip(']').lstrip().rstrip().lstrip("'").rstrip("'")
		    if str(i) not in phons:
    	    		form = WordForm()
	    		context = RequestContext(request,{'message':'Pls enter valid phoneme sequence','w':w,'m':M,'form':form})
    			if request.user.is_authenticated() :
    				template = loader.get_template('addword3.html')
    			else:
    				template = loader.get_template('addword3.html')
       	    		return HttpResponse(template.render(context))
		    else:
			p+=str(i)+'-'
		newword = Word(name = w, phomene =p[:-1])
		counter = False
        	try:
       			if request.FILES['audiofile']!='':
				newword.audiofile = request.FILES['audiofile']
				newword.save()
				obj_id = newword.pk
				counter = True
		except MultiValueDictKeyError:
		    	newword.audiofile = 'None'
		if counter :
			t1 = str(datetime.datetime.now().time())
			t2 = t1.split('.')

			d1 = str(datetime.datetime.now().date())
			d = d1.split('-')

			s1 =''
			s2 =''
			s3 =''

			char = string.ascii_uppercase
			c1 = [random.choice(char) for _ in range(4)]
			for i in c1:
			    s1 += i
			c2 = [random.choice(char) for _ in range(4)]
			for i in c2:
			    s2 += i
			c3 = [random.choice(char) for _ in range(3)]
			for i in c3:
			    s3 += i

			key = str(request.POST['w']) + '_' + 'i_' + str(obj_id) + '_' +t2[1] + s1 + d[2] + s2 + d[0] + d[1] + s3
		    	newword.key = key
			newword.save()
			newkey = WordKey(key = key,paid = False)
			newkey.save()


	else:
    	    form = WordForm()
	    context = RequestContext(request,{'message':'Pls enter phoneme sequence','w':w,'m':m,'form':form})
    	    if request.user.is_authenticated() :
    		template = loader.get_template('addword3.html')
    	    else:
    		template = loader.get_template('addword3.html')
       	    return HttpResponse(template.render(context))
	if counter:
	 if request.POST['pos']!='':
		newword.pos = request.POST['pos']
		newword.save()
	 if request.POST['meaning']!='':
		newword.meaning = request.POST['meaning']
		newword.save()
	 if request.POST['lang']!='':
		newword.origin = request.POST['lang']
		newword.save()
      #  form = WordForm(request.POST, request.FILES)
      #	if form.is_valid():
      #  record = Word.objects.filter(name__startswith=newword.name).order_by('-votes')
      #  list1= []
      #  if len(record)>0:
      #   for i in record:
#	  a = Word()
#	  a.pk = i.pk
#	  a.name = i.name
#	  a.phomene = i.phomene
#	  if i.audiofile=='':
#	    a.audiofile = 'None'
#	  else:
#	    a.audiofile= i.audiofile
#	  if i.pos=='':
#	    a.pos = 'None'
#	  else:
#	    a.pos= i.pos
#	  if i.origin=='':
#	    a.origin = 'None'
#	  else:
#	    a.origin= i.origin
#	  if i.meaning=='':
#	    a.meaning = 'None'
#	  else:
#	    a.meaning= i.meaning
#	  list1.append(a)
#	 context = RequestContext(request,{'record':list1,'w':newword.name})
	 context = RequestContext(request,{'key':newword.key,'w':newword.name})
    	 if request.user.is_authenticated() :
	     #template = loader.get_template('search.html')
	     template = loader.get_template('addword4.html')
    	 else:
	     #	template = loader.get_template('search.html')
	     	template = loader.get_template('addword4.html')
      	 return HttpResponse(template.render(context))
	else:
	    context = RequestContext(request,{'message': 'Please upload a file !!','w':w,'m':'[]'})
    	    if request.user.is_authenticated() :
    		template = loader.get_template('addword3.html')
    	    else:
	    	template = loader.get_template('addword3.html')
      	    return HttpResponse(template.render(context))

    else:
	 context = RequestContext(request)
    	 if request.user.is_authenticated() :
    		template = loader.get_template('search.html')
    	 else:
	    	template = loader.get_template('search.html')
      	 return HttpResponse(template.render(context))

def addword5(request):
    if request.method=='POST':
	w = request.POST['w']
	m = request.POST['m']
	recfile = request.POST['recfile']
	string = "wget " + str(recfile) + " -P /tmp/"
	os.system(string)
	context = RequestContext(request,{'w':w,'m':m,'recfile':recfile })
	template = loader.get_template('addword5.html')
	return HttpResponse(template.render(context))

def helper(request):
	context = RequestContext(request)
	template = loader.get_template('help.html')
	return HttpResponse(template.render(context))

def recording(request):
	context = RequestContext(request)
    	if request.user.is_authenticated() :
    		template = loader.get_template('record.html')
    	else:
    		template = loader.get_template('record.html')
        return HttpResponse(template.render(context))

def recording2(request):
    if request.method=='POST':
	data = request.POST['recfile']
	w = request.POST['w']
	context = RequestContext(request,{'data':data,'w':w})
    	template = loader.get_template('recording2.html')
        return HttpResponse(template.render(context))


def addreq(request):
    if request.method=='POST':
	form = RequestWordForm(request.POST, request.FILES)
	if form.is_valid():
		req = RequestWord(word = request.POST['name'])
		req.save()
		message = "Success!!"
	else:
	    message = "Unsuccessful ;("
    form = RequestWordForm()
    message = ""
    return render_to_response('addreq.html',{'form':form,'message':message},context_instance = RequestContext(request))

def displayallwords(request):
    #if request.user.is_authenticated() :
    words = Word.objects.all()
    list1 = []
    for w in words:
         if w.name not in list1:
             list1.append(w)
    if request.user.is_authenticated() :
       	template = loader.get_template('admin_displayallwords.html')
    else:
    	template = loader.get_template('displayallwords.html')
    list2 = []
    for i in list1:
	a = Word()
	a.name = i.name
	a.phomene = i.phomene
	if i.audiofile=='':
	    a.audiofile = 'None'
	else:
	    a.audiofile= i.audiofile
	if i.pos=='':
	    a.pos = 'None'
	else:
	    a.pos= i.pos
	if i.origin=='':
	    a.origin = 'None'
	else:
	    a.origin= i.origin
	if i.meaning=='':
	    a.meaning = 'None'
	else:
	    a.meaning= i.meaning
	list2.append(a)
    context = RequestContext(request, {'words': list2})
    return HttpResponse(template.render(context))
#else:
 #   template = loader.get_template('admin1.html')
  #  context = RequestContext(request)
  #  return HttpResponse(template.render(context))


def fest(request):
    flag = 0
    if request.user.is_authenticated() :
	flag = 1
    context = RequestContext(request,{'f' : flag})
    if request.user.is_authenticated() :
    	template = loader.get_template('fest.html')
    else:
    	template = loader.get_template('fest.html')
    return HttpResponse(template.render(context))

def fest2(request):
     word = str(request.POST['w'])
     try:
        null = open("/dev/null","w")
        subprocess.Popen("festival",stdout=null,stderr=null)
	null.close()
        string = 'echo "' + word + '" | festival --tts'
        os.system(string)
     except OSError:
	 context = RequestContext(request,{'message':''})
         template = loader.get_template('fest.html')

     if request.user.is_authenticated() :
     	 return HttpResponseRedirect(reverse('pname:fest'))
     else:
     	 return HttpResponseRedirect(reverse('pname:fest'))
  
def admin1(request):
    context = RequestContext(request)
    template = loader.get_template('admin1.html')
    return HttpResponse(template.render(context))

def admin2(request):
    if request.user.is_authenticated():
          context = RequestContext(request)
          template = loader.get_template('admin2.html')
          return HttpResponse(template.render(context))
    elif request.method=='POST':
    	username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)
    	if user is not None:
         if user.is_active:
                 login(request, user)
                 context = RequestContext(request)
                 template = loader.get_template('admin2.html')
                 return HttpResponse(template.render(context))
                 # Redirect to a success page
         else:
              # Return a 'disabled account' error message
               context = RequestContext(request)
               template = loader.get_template('admin1.html')
               return HttpResponse(template.render(context))
    	else:
        # Return an 'invalid login' error message.
        	message = "Invalid username/password"
        	context = RequestContext(request,{'message' : message})
        	template = loader.get_template('admin1.html')
        	return HttpResponse(template.render(context))
    else:
        	context = RequestContext(request)
        	template = loader.get_template('admin1.html')
        	return HttpResponse(template.render(context))



def adminlogout(request):
        logout(request)
	# context = RequestContext(request)
	# template = loader.get_template('home.html')
     	return HttpResponseRedirect(reverse('pname:home'))
    #return HttpResponse(template.render(context))

