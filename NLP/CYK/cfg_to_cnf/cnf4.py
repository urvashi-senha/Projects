# Extracts rules which have single non terminal
def func():	
	
	f = open('out3','r')
	text = f.readlines()
	f.close()
	
	f = open('out4','w')
	new_rule = []
	
	
	for t in text:
	    t = t[:-1]
	    rule, prob = t.split(' = ')
	    l,r = rule.split('->')
	    r = r.split()
	    if len(r) == 1:
		if str(r[-1]).isupper():
		    new_rule.append(t)
		
	   
	
	for i in new_rule:
		f.write(i)
		f.write('\n')
	f.close()
	
