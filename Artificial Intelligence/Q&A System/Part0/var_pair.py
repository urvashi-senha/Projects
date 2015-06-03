import nltk
#---------- query 1 -----------#

def var_pair1(winteam,pomteam):
   name_to_var = {}
   count = 0
   for i in winteam.values() :
	if i not in name_to_var:
	    name_to_var[i] = 't' + str(count)
	    count += 1

   for i in pomteam.values() :
	if i not in name_to_var:
	    name_to_var[i] = 't' + str(count)
	    count += 1
   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	    
   temp_strin1 = ''
   for i in name_to_var :
       temp_strin1 += i + ' => ' +name_to_var[i] + '\n'

   temp_strin4 = 'Match1 => m1\n'
   temp_strin4 += 'Match2 => m2\n'
   temp_strin4 += 'Match3 => m3\n'
   temp_strin4 += 'Match4 => m4\n'
   temp_strin4 += 'Match5 => m5\n'
   temp_strin4 += 'team => {t0,t1}\n'
   temp_strin4 += 'match => {m1,m2,m3,m4,m5}\n'

   temp_strin2 = 'winteam => {'
   for k,v in winteam.iteritems():
       temp_strin2 += '('
       temp_strin2 += k + ','
       temp_strin2 += name_to_var[v] + '),'
   temp_strin2 = temp_strin2[:-1]
   temp_strin2 += '} \n'

   temp_strin3 = 'pomteam => {'
   for k,v in pomteam.iteritems():
       temp_strin3 += '('
       temp_strin3 += k +','
       temp_strin3 += name_to_var[v] + '),'
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '}'

   v = temp_strin1 + temp_strin4 + temp_strin2 + temp_strin3
   query = 'all x.( (match(x) & exists y.(team(y) and (pomteam(x,y) and  winteam(x,y)))) | (-match(x)) )'
   parse = 'match(x) & exists y.(team(y) and (pomteam(x,y)) and winteam(x,y))'
   return  v,query,name_to_var,parse


#-------- query 2 ------------ #
def var_pair2(loseteam,duckteam):
   name_to_var = {}
   count = 0
   for i in loseteam.values() :
	if i not in name_to_var:
	    name_to_var[i] = 't' + str(count)
	    count += 1

   for i in duckteam.values() :
	if i not in name_to_var:
	    name_to_var[i] = 't' + str(count)
	    count += 1
   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	    
   temp_strin1 = ''
   for i in name_to_var :
       temp_strin1 += i + ' => ' +name_to_var[i] + '\n'

   temp_strin4 = 'Match1 => m1\n'
   temp_strin4 += 'Match2 => m2\n'
   temp_strin4 += 'Match3 => m3\n'
   temp_strin4 += 'Match4 => m4\n'
   temp_strin4 += 'Match5 => m5\n'
   temp_strin4 += 'team => {t0,t1}\n'
   temp_strin4 += 'match => {m1,m2,m3,m4,m5}\n'


   temp_strin2 = 'loseteam => {'
   for k,v in loseteam.iteritems():
       temp_strin2 += '('
       temp_strin2 += k + ','
       temp_strin2 += name_to_var[v] + '),'
   temp_strin2 = temp_strin2[:-1]
   temp_strin2 += '} \n'
   
   temp_strin3 = 'duckteam => {'
   for k,v in duckteam.iteritems():
       temp_strin3 += '('
       temp_strin3 += k + ','
       temp_strin3 += name_to_var[v] + '),'
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '} \n'
   
   v = temp_strin1 + temp_strin4 + temp_strin2 + temp_strin3
   query = 'all x.( (match(x) & exists y.(team(y) and (duckteam(x,y) and  loseteam(x,y)))) | (-match(x)) )'
   parse = 'match(x) & exists y.(team(y) and duckteam(x,y) and loseteam(x,y))' 
   return  v,query,name_to_var,parse

#-------- query 3--------------#
def var_pair3(strikeplayer,sixplayer):
	name_to_var = {}
   	string1='Innings1 => in1\nInnings2 =>in2\nInnings3 => in3\nInnings4 =>in4\nInnings6 => in6\nInnings7 =>in7\nInnings8 => in8\nInnings9 =>in9\nInnings10 =>in10\n'
	p=[]
   	for i in strikeplayer.values():
		for j in i:
			if j not in p:
	    			p.append(j)
	for i in sixplayer.values():
		for j in i:
			if i not in p:
				p.append(j)
	string2='player => {'
#	print p
	for i in p:
		string2+=i+','
	string2 =string2[:-1]
	string2+='}\n'
   	name_to_var['Innings1'] = 'in1'	    
   	name_to_var['Innings2'] = 'in2'	    
   	name_to_var['Innings3'] = 'in3'	    
   	name_to_var['Innings4'] = 'in4'	    
   	name_to_var['Innings5'] = 'in5'	    
   	name_to_var['Innings6'] = 'in6'	    
   	name_to_var['Innings7'] = 'in7'	    
   	name_to_var['Innings8'] = 'in8'	    
   	name_to_var['Innings9'] = 'in9'	    
   	name_to_var['Innings10'] = 'in10'
	string3='match => {in1,in2,in3,in4,in5,in6,in7,in8,in9,in10}\n'
   	string4 = 'strikeplayer => {'
   	for k,v in strikeplayer.iteritems():
		for i in v:
       			string4 += '('
       			string4 += k +','
       			string4 += i + '),'
   	string4 = string4[:-1]
   	string4 += '}\n'
   	string5 = 'sixplayer => {'
   	for k,v in sixplayer.iteritems():
		for i in v:
       			string5 += '('
       			string5 += k +','
       			string5 += i + '),'
   	string5 = string5[:-1]
   	string5 += '}\n'

	v=''
	v=string1+string2+string3+string4+string5
	query='all x.( (match(x) & all y.((player(y) and ((strikeplayer(x,y) &  sixplayer(x,y))|(-strikeplayer(x,y))))|(-player(y)))) | (-match(x)) )'
	parse='match(x) & all y.((player(y) and strikeplayer(x,y) -> sixplayer(x,y)|-player(y)))'	
   	return  v,query,name_to_var,parse



#---------query 4---------#
def var_pair4(boundary,strikerate):

   name_to_var = {}
   count = 0
   for i in boundary.values() :
	   for j in i:
		if j not in name_to_var:
	    		name_to_var[j] = 'p' + str(count)
	    		count += 1

   for i in strikerate.values() :
	   for j in i:
		   if j not in name_to_var:
	    		name_to_var[j] = 'p' + str(count)
	    		count += 1

   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	    
   temp_strin2 = ''
   for i in name_to_var :
       temp_strin2 += i + ' => ' +name_to_var[i] + '\n'


   temp_strin1 = ''
   temp_strin1 += 'player => {'
   for i in name_to_var:
	   temp_strin1 += name_to_var[i]
	   temp_strin1 += ','
   temp_strin1 = temp_strin1[:-1]
   temp_strin1 += '} \n'
   temp_strin1 += 'Match1 => m1\n'
   temp_strin1 += 'Match2 => m2\n'
   temp_strin1 += 'Match3 => m3\n'
   temp_strin1 += 'Match4 => m4\n'
   temp_strin1 += 'Match5 => m5\n'
   temp_strin1 += 'match => {m1,m2,m3,m4,m5}\n'




   temp_strin3 = 'boundary => {'
   for k,v in boundary.iteritems():
	   for j in v:
       		temp_strin3 += '('
       		temp_strin3 += k + ','
       		temp_strin3 += name_to_var[j] + '),'
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '} \n'


   temp_strin4 = 'strikerate => {'
   for k,v in strikerate.iteritems():
	   for j in v:
       		temp_strin4 += '('
       		temp_strin4 += k + ','
       		temp_strin4 += name_to_var[j] + '),'
   temp_strin4 = temp_strin4[:-1]
   temp_strin4 += '} \n'

   v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4

   query = 'all x.( (match(x) & exists y.((player(y) and (boundary(x,y) and strikerate(x,y))))) | (-match(x)))'
   parse = '(match(x) & exists y.((player(y) and (boundary(x,y) and strikerate(x,y)))))'
   return  v,query,name_to_var,parse


#------------- query 5 --------------#
def var_pair5(batplayer,wicketplayer):
   name_to_var = {}
   count = 0
   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	    
   
   for i in batplayer :
        v = batplayer[i]
	for u in v:
		if u not in name_to_var:
	    		name_to_var[u] = 'p' + str(count)
	    		count += 1

   for i in wicketplayer :
        v = wicketplayer[i]
	for u in v:
		if u not in name_to_var:
	    		name_to_var[u] = 'p' + str(count)
	    		count += 1
   temp_strin1 = ''
   for i in name_to_var :
       temp_strin1 += i + ' => ' +name_to_var[i] + '\n'
   
   #temp_strin4 = 'Match1 => m1\n'
   #temp_strin4 += 'Match2 => m2\n'
   #temp_strin4 += 'Match3 => m3\n'
   #temp_strin4 += 'Match4 => m4\n'
   #temp_strin4 += 'Match5 => m5\n'
   temp_strin4 = 'match => {m1,m2,m3,m4,m5}\n'

   temp_strin5 = 'player => {'
   for c in range(count):
  	 temp_strin5 += 'p' + str(c) + ','
   temp_strin5 = temp_strin5[:-1]
   temp_strin5 += '}\n'

   
   temp_strin2 = 'batplayer => {'
   for i in batplayer:
       v = batplayer[i]
       for u in v:
       	temp_strin2 += '('
      	temp_strin2 += i + ','
       	temp_strin2 += name_to_var[u] + '),'
   
   temp_strin2 = temp_strin2[:-1]
   temp_strin2 += '} \n'
   
   temp_strin3 = 'wicketplayer => {'
   for i in wicketplayer:
       v = wicketplayer[i]
       for u in v:
       	temp_strin3 += '('
      	temp_strin3 += i + ','
       	temp_strin3 += name_to_var[u] + '),'
   
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '} \n'
   
   v = temp_strin1 + temp_strin4 + temp_strin5 +temp_strin2 + temp_strin3
   query = 'all x.( (match(x) & exists y.((player(y) and (batplayer(x,y) and wicketplayer(x,y))))) | (-match(x)) )' 
   parse = 'match(x) & exists y.(player(y) and batplayer(x,y) and wicketplayer(x,y))' 
   return  v,query,name_to_var,parse

#-----------------query 6----#

def var_pair6(bowlmorethan7,nowicket):
   name_to_var = {}
   count = 0
   temp_strin1=''
   temp_strin2=''
   temp_strin3=''
   temp_strin4=''
   temp_strin5=''
   for i in bowlmorethan7.values() :
        for j in i:
	 if j not in name_to_var:
	    name_to_var[j] = 'p' + str(count)
	    count += 1

   for i in nowicket.values() :
        for j in i:
	 if j not in name_to_var:
	    name_to_var[j] = 'p' + str(count)
	    count += 1
   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	    
   for i in name_to_var :
       temp_strin1 += i + ' => ' +name_to_var[i] + '\n'
   temp_strin2 += 'match'+ '=>'+ '{m1,m2,m3,m4,m5}\n'
   player=[]
	
   
   
   for i in bowlmorethan7.values() :
        for j in i:
	  if j not in player:
          	player.append(j)
           #temp_strin3 += name_to_var[j] + ','
   for i in nowicket.values():
        for j in i:
	  if j not in player:
		player.append(j)
   temp_strin2 += 'player => {'
   for i in player:
	temp_strin3 += name_to_var[i] + ','
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 +='}\n'
   temp_strin4='bowlmorethan7 => {'
   for k,v in bowlmorethan7.iteritems():
         for i in v:
           temp_strin4 +='('+k+','+name_to_var[i]+')'+','  
   temp_strin4 = temp_strin4[:-1]
   temp_strin4 += '} \n'
   temp_strin5='nowicket => {'
   for k,v in nowicket.iteritems():
         for i in v:
           temp_strin5 +='('+k+','+name_to_var[i]+')'+','  
   temp_strin5 = temp_strin5[:-1]
   temp_strin5 += '} \n'
   v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4 + temp_strin5
   query = 'all x.( (match(x) & exists y.((player(y) and (bowlmorethan7(x,y) and nowicket(x,y))))) | (-match(x)) )'
   parse = 'match(x) & exists y.(player(y) and bowlmorethan7(x,y) and nowicket(x,y))'
   return  v,query,name_to_var,parse
  


#----------query 7----------#
def var_pair7(wicket,economy):

   name_to_var = {}
   count = 0
   for i in economy.values() :
	   for j in i:
		if j not in name_to_var:
	    		name_to_var[j] = 'p' + str(count)
	    		count += 1

   for i in wicket.values() :
	   for j in i:
		if j not in name_to_var:
	    		name_to_var[j] = 'p' + str(count)
	    		count += 1

   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	     
   temp_strin2 = ''
   for i in name_to_var :
       temp_strin2 += i + ' => ' +name_to_var[i] + '\n'


   temp_strin1 = ''
   temp_strin1 += 'player => {'
   for i in name_to_var:
	   temp_strin1 += name_to_var[i]
	   temp_strin1 += ','
   temp_strin1 = temp_strin1[:-1]
   temp_strin1 += '} \n'
   temp_strin1 += 'Match1 => m1\n'
   temp_strin1 += 'Match2 => m2\n'
   temp_strin1 += 'Match3 => m3\n'
   temp_strin1 += 'Match4 => m4\n'
   temp_strin1 += 'Match5 => m5\n'
   temp_strin1 += 'match => {m1,m2,m3,m4,m5}\n'




   temp_strin3 = 'wicket => {'
   for k,v in wicket.iteritems():
	   for j in v:
       		temp_strin3 += '('
       		temp_strin3 += k + ','
       		temp_strin3 += name_to_var[j] + '),'
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '} \n'


   temp_strin4 = 'economy => {'
   for k,v in economy.iteritems():
	   for j in v:
       		temp_strin4 += '('
       		temp_strin4 += k + ','
       		temp_strin4 += name_to_var[j] + '),'
   temp_strin4 = temp_strin4[:-1]
   temp_strin4 += '} \n'

   v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4

   query = 'all x.(match(x) & (exists y.((player(y) & (wicket(x,y) & economy(x,y))))) | -match(x))'
   parse = 'match(x) & (exists y.((player(y) & (wicket(x,y) & economy(x,y)))))'
   return  v,query,name_to_var,parse


#--------------- query 8 ---------------#

def var_pair8(team100,loseteam):
   
   name_to_var = {}
   count = 0
   
   for i in team100 :
        v = team100[i]
	for u in v:
		if u not in name_to_var:
	    		name_to_var[u] = 't' + str(count)
	    		count += 1
   for i in loseteam.values():
	if i not in name_to_var:
	    		name_to_var[i] = 't' + str(count)
	    		count += 1
   
   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	    
   
   temp_strin1 = ''
   for i in name_to_var :
       temp_strin1 += i + ' => ' +name_to_var[i] + '\n'
   
   temp_strin4 = 'match => {m1,m2,m3,m4,m5}\n'
   temp_strin4 += 'team => {t0,t1}\n'


   temp_strin2 = 'team100 => {'
   for i in team100:
       v = team100[i]
       for u in v:
       	temp_strin2 += '('
      	temp_strin2 += i + ','
       	temp_strin2 += name_to_var[u] + '),'
   
   temp_strin2 = temp_strin2[:-1]
   temp_strin2 += '} \n'


   temp_strin3 = 'loseteam => {'
   for k,v in loseteam.iteritems():
       	temp_strin3 += '('
      	temp_strin3 += k + ','
       	temp_strin3 += name_to_var[v] + '),'
   
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '} \n'
   
   v = temp_strin1 + temp_strin4 + temp_strin2 + temp_strin3
   query = 'exists x.(match(x) & exists y.((team(y) and (team100(x,y) and loseteam(x,y)))))' 
   parse = 'match(x) & exists y.(team(y) and team100(x,y) and loseteam(x,y))'
   return  v,query,name_to_var,parse

#------------------ query 9 ----------------#

def var_pair9(wicket):

   name_to_var ={}

   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	  

   temp_strin1 = ''	   
   for i in name_to_var:
       temp_strin1 += i + ' => '+ name_to_var[i] +'\n'

   temp_strin2 = 'Right => r\nLeft=> l\nmatch => {m1,m2,m3,m4,m5}\nhand => {l,r}\nequal => {(m1,r),(m2,r),(m3,r),(m4,r),(m5,r)}\n'

   temp_strin3 = 'wicket => {'
   for i in wicket:
       temp_strin3 += '(' + i + ',' + wicket[i] + '),'
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '}\n'

   v = temp_strin1 + temp_strin2 +temp_strin3

   query = 'all x.( (match(x) & exists y.( hand(y) & wicket(x,y) & equal(x,y)) )  | (-match(x)))'
   parse = ' (match(x) & exists y.( hand(y) & wicket(x,y) & equal(x,y))) '

   return v,query,parse,name_to_var



#--------- query 10 ---------------#

def var_pair10(score250,age26,duck):

   name_to_var = {}
   count =0
   for i in score250:
	name_to_var[i] = 'p' + str(count)
	count += 1
   for i in age26:
	name_to_var[i] = 'p' + str(count) 
	count += 1
   for i in duck:
	name_to_var[i] = 'p' + str(count)
	count += 1

   temp_strin1 = ''
   for i in name_to_var :
       temp_strin1 += i + ' => ' +name_to_var[i] + '\n'

   temp_strin2 = 'score250 => {'
   for i in score250:
       temp_strin2 += name_to_var[i] + ','
   temp_strin2 = temp_strin2[:-1]
   temp_strin2 += '}\n'
   
   temp_strin3 = 'age26 => {'
   for i in age26:
       temp_strin3 += name_to_var[i] + ','
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '}\n'
   

   temp_strin4 = 'duck => {'
   for i in duck:
       temp_strin4 += name_to_var[i] + ','
   temp_strin4 = temp_strin4[:-1]
   temp_strin4 += '}'

   v = temp_strin1 + temp_strin2 + temp_strin3 + temp_strin4
   query = 'exists x.(age26(x) & score250(x) & -duck(x) )'
   parse = 'age26(x) & score250(x) & -duck(x) '
   return v,query,parse,name_to_var


#--------------------------query 11------------------------------------

def var_pair11(match1):
	string1='play1 => {'
	for i in match1['play1']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play2 => {'
	for i in match1['play2']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play3 => {'
	for i in match1['play3']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play4 => {'
	for i in match1['play4']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	string1+='play5 => {'
	for i in match1['play5']:
		string1+=i+','
	string1=string1[:-1]
	string1+='}\n'
	
	query='play1(x) and play2(x) and play3(x) and play4(x) and play5(x)'
	l = nltk.LogicParser()
	val = nltk.parse_valuation(string1)
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	g = nltk.Assignment(dom,[])
	
	fmla1 = l.parse(query)
	print m.satisfiers(fmla1, 'x' ,g)


#--------------------query12-----------------------------------------------	
def var_pair12(wideplayer):
   	string4 = 'wideplayer => {'
   	for k,v in wideplayer.iteritems():
		for i in v:
       			string4 += '('
       			string4 += k +','
       			string4 += i + '),'
   	string4 = string4[:-1]
   	string4 += '}'
   	
	v=''
	v=string4
	#print v
	#query='wideplayer(I Sharma,RA Jadeja)'
	parse=''	
   	val = nltk.parse_valuation(v)
	#print val
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	g = nltk.Assignment(dom,[('x','I Sharma'),('y','RA Jadeja')])
	print "************************"
	print m.evaluate('wideplayer(x,y)', g)
	print "************************"
	

#------query 13-----#
def var_pair13(highrun):

   name_to_var = {}
   temp_strin3 = 'highrun => {'
   for k,v in highrun.iteritems():
	   for j in v:
       		temp_strin3 += '('
       		temp_strin3 += k + ','
       		temp_strin3 += j + '),'
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '} \n'

   v = temp_strin3 

   query = 'highrun(x,y)'
   #parse = 'highrun(Ryder,Southee)'
   #return  v,query,name_to_var,parse

   l = nltk.LogicParser()
   val = nltk.parse_valuation(v)

   dom = val.domain
   m = nltk.Model(dom,val)
   dom = m.domain
   g = nltk.Assignment(dom,[('x','Ryder'),('y','Southee')])
   print "******************************"
   print m.evaluate(query,g)
   print "**************************"


#----------------------------query14-----------------------------------------

def var_pair14(mop):
	name_to_var={}
	string2='player => {'    			
	for i in mop.values():
		string2+=i+','
	string2 =string2[:-1]
	string2+='}\n'

   	name_to_var['Match1'] = 'm1'	    
   	name_to_var['Match2'] = 'm2'	    
   	name_to_var['Match3'] = 'm3'	    
   	name_to_var['Match4'] = 'm4'	    
   	name_to_var['Match5'] = 'm5'

	string3='Match1 => m1\nMatch2 => m2\nMatch3 => m3\nMatch4 => m4\nMatch5 => m5\n'
        string3+='match => {m1,m2,m3,m4,m5}\n'
	string3+='equal => {(m1,m1),(m2,m2),(m3,m3),(m4,m4),(m5,m5)}\n' 

	string4='mop => {'
	for i in mop:
		string4+='('+i+','+mop[i]+'),'
	string4=string4[:-1]
	string4+='}\n'
	v=''
	v=string2+string3+string4

	query='exists x. exists y. exists z.(match(x) and match(y) and player(z) and mop(x,z) and mop(y,z) and -equal(x,y))'

	val = nltk.parse_valuation(v)
	#print val
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	g = nltk.Assignment(dom,[])
	print "************************"
	print m.evaluate(query, g)
	print "************************"


#------------- query 15 -------------------#
def var_pair15(inn1,inn2):

   name_to_var = {}
   count = 0
   for i in inn1:
	if i not in name_to_var:
	    name_to_var[i] = 'p' + str(count)
	    count += 1
   for i in inn2:
	if i not in name_to_var:
	    name_to_var[i] = 'p' + str(count)
	    count += 1

   temp_strin1 = ''
   for i in name_to_var :
       temp_strin1 += i + ' => ' +name_to_var[i] + '\n'

   temp_strin4 = 'player =>{'
   for c in range(count):
       temp_strin4 += 'p' + str(c) + ','
   temp_strin4 = temp_strin4[:-1]
   temp_strin4 += '}\n'

   temp_strin2 = 'inn1 => {'
   for i in inn1:
       temp_strin2 += name_to_var[i] + ','
   temp_strin2 = temp_strin2[:-1]
   temp_strin2 += '}\n'
   
   temp_strin3 = 'inn2 => {'
   for i in inn2:
       temp_strin3 += name_to_var[i] + ','
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '}\n'

   v = temp_strin1 + temp_strin4 +temp_strin2 + temp_strin3
   l = nltk.LogicParser()
	
   val = nltk.parse_valuation(v)
   #print val

   dom=val.domain
   m = nltk.Model(dom , val)
   dom=m.domain
   #print dom
   bowler = name_to_var['RA Jadeja']
   g = nltk.Assignment(dom,[('x',bowler)])
   #print g	
   print "************************"
   #print m.evaluate('all x.( (match(x) & exists y.(team(y) and (pomteam(x,y) and  winteam(x,y)))) | (-match(x)) )', g)
   flag1 = m.evaluate(' player(x) and inn1(x) ', g)
   flag2 = m.evaluate(' player(x) and inn2(x) ', g)
   if(flag1 == True):
   	print 'Inning 1'
   else:
       print ' Inning 2'

   print "************************"

#---------query 16---------#
def var_pair16(arr):
	name_to_var = {}
	count = 0
	for i in arr :
		if i not in name_to_var:
			name_to_var[i] = 'p'+str(count)
			count = count+1
	st = 'MS Dhoni'
   	temp_strin1 = ''
   	temp_strin1 += 'player => {'
   	for i in name_to_var:
	   temp_strin1 += name_to_var[i]
	   temp_strin1 += ','
   	temp_strin1 = temp_strin1[:-1]
   	temp_strin1 += '} \n'
	if st not in name_to_var:
		name_to_var[st]='p'+str(count)
		count = count+1
	s = name_to_var['MS Dhoni']

   	v = temp_strin1
   	query = 'player(s)'

   	l = nltk.LogicParser()
   	val = nltk.parse_valuation(v)

   	dom = val.domain
   	m = nltk.Model(dom,val)
   	dom = m.domain
   	g = nltk.Assignment(dom,[('s',name_to_var['MS Dhoni'])])
   	print "******************************"
   	print m.evaluate(query,g)
	print "******************************"

#-------- query 17 ------------- #
def var_pair17(bowlplayer):
	string4='bowlplayer => {'
	for k,v in bowlplayer.iteritems():
		for i in v:
			string4 += '('+k + ',' + i + '),'
	string4=string4[:-1]
	string4+='}\n'
	v=string4
	
	val=nltk.parse_valuation(v)
	dom=val.domain
	m=nltk.Model(dom , val)
	dom=m.domain
	g=nltk.Assignment(dom,[('x','RA Jadeja'),('y','I Sharma')])
	print "***********************************************"
	print m.evaluate('bowlplayer(x,y)',g)
	print "***********************************************"


#----------------------------query 18 -----------------------------

def var_pair18(middle,count):
	
	string1='Batsmen => {'
	for k in middle:
		string1+= k +','
	string1=string1[:-1]
	string1+='}\n'
	
	v=string1
	
	query='Batsmen(x)'
	
	l = nltk.LogicParser()
	
	val = nltk.parse_valuation(v)
	
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	g = nltk.Assignment(dom,[])
	
	
	fmla1 = l.parse(query)
	varnames = m.satisfiers(fmla1, 'x' ,g)

	le=len(varnames)
	le=le/count
	if le>=0.8:
		print True
	else:
		print False

#----------------------------query19--------------------------------------------

def var_pair19(winteam,tossteam):
   	name_to_var = {}
   	count = 0
	#print winteam
   	for i in winteam.values() :
		if i not in name_to_var:
			name_to_var[i] = 't' + str(count)
	    		count += 1
	
   	for i in tossteam.values() :
		if i not in name_to_var:
	    		name_to_var[i] = 't' + str(count)
	    		count += 1

   	name_to_var['Match1'] = 'm1'	    
   	name_to_var['Match2'] = 'm2'	    
   	name_to_var['Match3'] = 'm3'	    
   	name_to_var['Match4'] = 'm4'	    
   	name_to_var['Match5'] = 'm5'	    
   	temp_strin1 = ''

   	for i in name_to_var :
       		temp_strin1 += i + ' => ' +name_to_var[i] + '\n'

   	temp_strin4 = 'Match1 => m1\n'
   	temp_strin4 += 'Match2 => m2\n'
   	temp_strin4 += 'Match3 => m3\n'
   	temp_strin4 += 'Match4 => m4\n'
   	temp_strin4 += 'Match5 => m5\n'
   	temp_strin4 += 'team => {t0,t1}\n'
   	temp_strin4 += 'match => {m1,m2,m3,m4,m5}\n'

   	temp_strin2 = 'winteam => {'
   	for k,v in winteam.iteritems():
       		temp_strin2 += '('
       		temp_strin2 += k + ','
       		temp_strin2 += name_to_var[v] + '),'
   	temp_strin2 = temp_strin2[:-1]
   	temp_strin2 += '} \n'

   	temp_strin3 = 'tossteam => {'
   	for k,v in tossteam.iteritems():
       		temp_strin3 += '('
       		temp_strin3 += k +','
       		temp_strin3 += name_to_var[v] + '),'
   	temp_strin3 = temp_strin3[:-1]
   	temp_strin3 += '}'

   	v = temp_strin1 + temp_strin4 + temp_strin2 + temp_strin3
   	query = 'all x.( (match(x) & exists y.(team(y) and (tossteam(x,y) and winteam(x,y)))) | (-match(x)) )'
	val = nltk.parse_valuation(v)
	#print val
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	g = nltk.Assignment(dom,[])
	print "************************"
	print m.evaluate(query, g)
	print "************************"

	
#-------query 20-------#

def var_pair20(winteam):

   name_to_var = {}
   name_to_var['Match1'] = 'm1'	    
   name_to_var['Match2'] = 'm2'	    
   name_to_var['Match3'] = 'm3'	    
   name_to_var['Match4'] = 'm4'	    
   name_to_var['Match5'] = 'm5'	     
   temp_strin2 = ''
   for i in name_to_var :
       temp_strin2 += i + ' => ' +name_to_var[i] + '\n'

   temp_strin3 = 'winteam => {'
   for k,v in winteam.iteritems():
       	temp_strin3 += '('
       	temp_strin3 += k + ','
       	temp_strin3 += v + '),'
   temp_strin3 = temp_strin3[:-1]
   temp_strin3 += '} \n'

   
   temp_strin4 = 'Match1 => m1\n'
   temp_strin4 += 'Match2 => m2\n'
   temp_strin4 += 'Match3 => m3\n'
   temp_strin4 += 'Match4 => m4\n'
   temp_strin4 += 'Match5 => m5\n'
   temp_strin4 += 'match => {m1,m2,m3,m4,m5}\n'

   v = temp_strin3 + temp_strin4 + temp_strin2

   parse1 = 'match(x) & winteam(x,i)'
   parse2 = 'match(x) & winteam(x,n) | -match(x)'
   #return  v,query,name_to_var,parse

   l = nltk.LogicParser()
   val = nltk.parse_valuation(v)

   dom = val.domain
   m = nltk.Model(dom,val)
   dom = m.domain
   g = nltk.Assignment(dom,[('i','India'),('n','New Zealand')])
   print "******************************"
   fmla1 = l.parse(parse1)
   varnames1 = m.satisfiers(fmla1, 'x' , g)
   fmla2 = l.parse(parse2)
   varnames2 = m.satisfiers(fmla2, 'x' , g)
   #print varnames1
   #print varnames2
   count1=0
   count2=0
   for i in varnames1:
	   for p,q in winteam.iteritems():
		   if p == i:
			   count1 = count1+1
   for i in varnames2:
	   for p,q in winteam.iteritems():
		   if p == i:
			   count2 = count2+1
   if count1 > count2:
	print 'India'
   else:
	print 'New Zealand'
   print "**************************"

	
