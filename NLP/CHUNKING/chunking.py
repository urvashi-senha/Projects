import codecs
from Queue import *

queue = Queue(maxsize=0)
stack = []


sentence = 'Red_JJ figures_NN on_IN the_DET screen_NN indicated_VB falling_JJ stocks_NN'
#sentence = 'The_DET man_NN saw_VB the_DET girl_NN at_IN the_DET party_NN'
#sentence = 'The_DET man_NN at_IN the_DET party_NN saw_VB the_DET girl_NN'
rules = ['NP -> JJ NN','NP -> DET NN','PP -> IN NP','VP -> VB NP','NP -> NP PP','VP -> VP PP']
#rules = ['NP -> NN PSPP','PSPP -> NN PSP','VP -> VAUX VAUX','VP -> VM VP']

sent = sentence.split()


for i in sent:
    	tu = ['None' , i]
	queue.put(tu)

stack_head = None
queue_head = None
flag =0


stack.append(queue.get())

while not queue.empty() or flag ==1:

    #   print'****************'
   #print flag
   if flag == 0:
    left1 = stack.pop()
    right1 = queue.get()
   
   stack_head = left1[0]
   if stack_head == 'None':
   	stack_head = left1[1].split('_')[1]
   
   queue_head = right1[0]
   if queue_head == 'None':
   	queue_head = right1[1].split('_')[1]
   
   #print stack_head,queue_head   
   
   flag =0
   for rule in rules:
       l,r = rule.split(' -> ')
       l = l.strip()
       r = r.split()
       if stack_head == r[0].strip() and queue_head == r[1].strip():
	   #	   print rule
	   flag = 1
	   temp_tu = []
	   temp_tu.append(l)
	   if left1[0] == 'None':
	   	temp_tu.append(left1[1:])
	   else:
	       temp_tu.append(left1)
	   if right1[0] == 'None':
	   	temp_tu.append(right1[1:])
	   else:
	   	temp_tu.append(right1)

	   stack.append(temp_tu)
	   #print stack
  
   if flag == 0 :
       stack.append(left1)
       stack.append(right1)

   if flag == 1 and len(stack) > 1:
       #print 'here'
	  right1 = stack.pop()
	  left1 = stack.pop()
   else:
       flag = 0

	 
#   print stack
    
print stack



