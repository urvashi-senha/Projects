## given rules, cal probability of rules
	
from collections import Counter
def func():	
	f = open('out','r')
	text = f.readlines()
	f.close()
	f = open('out2','w')
	
	left_head = []
	new_rule = []
	
	for t in text:
	    t = t[:-1]
	    l,r = t.split('->')
	    left_head.append(l.strip())
	    new_rule.append(t.strip())
	
	a = Counter(left_head)
	a = a.most_common()
	a = list(a)
	b = Counter(new_rule)
	b = b.most_common()
	b = list(b)
	
	
	rules =[]
	for t in text:
	    t = t[:-1]
	    l,r = t.split('->')
	    for i,j in b:
		if str(i.strip())==str(t.strip()):
	    		num = j*1.0
			break
	    for i,j in a:
		if str(i.strip())==str(l.strip()):
	    		den = j*1.0
			break
	    p = num/den
	    s = t + ' = ' + str(p)
	    if s not in rules:
	    	rules.append(s)
	
	for i in rules:
	    f.write(i)
	    f.write('\n')
	
	   
	
