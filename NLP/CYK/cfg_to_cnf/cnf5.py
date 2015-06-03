## rules giving singular non-terminals are replaced
## Eg: NP -> NN, S -> NP VP becomes S-> NN VP , S -> NP VP
def func():	
	f = open('out4','r')
	text1 = f.readlines()
	f.close()
	g = open('out3','r')
	text2 = g.readlines()
	g.close()
	h =open('rules_cnf.txt','w')
	new_rule = []
	count =1
	for t1 in text1:
	    t1 = t1[:-1]
	    rule1, prob1 = t1.split('=')
	    rule1=rule1.strip()
	    prob1 = prob1.strip()
	    l1,r1 = rule1.split('->')
	    l1 = l1.strip()
	    r1 = r1.strip()
	    for t2 in text2:
		t2=t2[:-1]
		rule2, prob2 = t2.split('=')
		rule2=rule2.strip()
		prob2=prob2.strip()
		l2,r2 = t2.split('->')
		r2 = r2.split()
		if len(r2) > 1:
		 if l1 in r2:
		    
		    p = float(prob1)*float(prob2)
		    if l1 == r2[0].strip() and l1 == r2[1].strip():
		    	s  = l2.strip() + ' -> ' +  r1.strip() + ' ' + r1.strip() + ' = ' + str(p)
			if s not in new_rule:
				
				new_rule.append(s)
		    if l1 == r2[0].strip():
		    	s  = l2.strip() + ' -> ' +  r1.strip() + ' ' + r2[1] + ' = ' + str(p)
			if s not in new_rule:
				new_rule.append(s)
				
		    if l1 == r2[1].strip():
		    	s  = l2.strip() + ' -> ' +  r2[0] + ' ' + r1.strip() + ' = ' + str(p)
			if s not in new_rule:
				new_rule.append(s)
				
		  
	for i in new_rule:
	    i = i.replace('= =','=')
	   
	    h.write(i)
	    h.write('\n')
	h.close()
	
	
