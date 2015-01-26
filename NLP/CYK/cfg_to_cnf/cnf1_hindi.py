## Given chunked sentences , outputs rules in CFG format
## Eg 
def func(fname):	
	f = open(fname,"r")
	#f = open('a.txt',"r")
	text = f.readlines()
	f.close()
	
	f  = open('out','w')
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
				if len(temp) == 2 and temp[0].isupper() and temp[1].isupper():
				    temp.reverse()
				elif len(temp)>2:
				    temp.reverse()
				if len(temp) > 0:
					rul = temp[0] + ' -> '
					for k in temp[1:]:
				   		 rul += k + ' '
					stack.append(temp[0])
					if rul not in rule:
						rule.append(rul)
						f.write(rul)
						f.write('\n')
				
	f.close()
	
	
	
	
					
				
				
		
