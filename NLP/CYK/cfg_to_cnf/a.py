stack = []
rule = []
t = '(ROOT (SQ (VBZ Is) (NP (DT this)) (NP (DT a) (NN book)) (. ?)))'
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
				rul = temp[0] + ' --> '
				for k in temp[1:]:
						rul += k + ' '
				stack.append(temp[0])
				if rul not in rule:
						rule.append(rul)
	
print rule

