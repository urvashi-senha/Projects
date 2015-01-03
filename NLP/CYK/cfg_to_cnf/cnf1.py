## Given chunked sentences , outputs rules in CFG format
## Eg (ROOT (S (NP (DT This)) (VP (VBZ is) (NP (DT a) (NN book))) (. .)))
def func(fname):	
	f = open(fname,"r")
	text = f.readlines()
	f.close()
	f = open('out','w')
	stack = []
	rule = []
	
	for t in text:
		t = t.replace('(','( ').replace(')',' )')
		t = t[:-1]
		t = t.split()
		for i in t :
			if str(i) !=')':
				stack.append(str(i))
			elif str(i)==')':
				temp = []
				rul = ''
				while(stack[len(stack)-1]!='('):
					temp.append(stack.pop())
				stack.pop()
				temp.reverse()
				rul = temp[0] + ' -> '
				for k in temp[1:]:
						rul += k + ' '
				stack.append(temp[0])
				if rul not in rule:
						rule.append(rul)
						f.write(rul)
						f.write('\n')
	



				
			
			
	
