### Given a list of tags and set of rules outputs the 
### index of each span and where it breaks
### Eg : 1 3 NP: 2 DET NN 

def build_tree(tags,model):
    print tags
    terminals = set(tags)
    pi = {} # pi[start,end,tags[start to end]] = prob  
    back = {}
    n = len(tags) #sentence length

#pi2 prob for each span variation,pi2 is out chart pi2[row][col][starting symbol]
    pi2 ={}
    for i in range(0,n+1):
	pi2[i] = {}
	for j in range(i+1,n+1):
	    pi2[i][j] = {}
   
    for i in range(1,n+1):
	pi2[i-1,i,tags[i-1]] = 1.0
	pi2[i-1][i][tags[i-1]] = 1.0

# selecting rules relating to tags in our sentence
    model2 = {}
    for i in model:
	left,right = i.split('->')
	left = left.strip()
	right= right.split()
	if len(right) > 1:
	    model2[left,right[0],right[1]] = model[i]
# processing the chart
    for i in range(2,n+1):	#total span
       for j in range(0,n-i+1): 	#left span start
	   for k in range(j+1,j+i):		#partition index
	       for rule in model2:
		   A,B,C = rule
		   if B not in pi2[j][k]:
		   	continue
		   if C not in pi2[k][j+i]:
		       continue
		   #print  pi2[j][k][B],  pi2[k][i+j][C], model2[rule]
		   prob = float(pi2[j][k][B]) * float(pi2[k][i+j][C]) * float(model2[rule])

		   if A not in pi2[j][i+j] or pi2[j][i+j][A] < prob :
			pi2[j][j+i][A] = prob
   			back[(j,i+j,A)] = (k,B,C)
			print str(j) + ' ' + str(i+j) + ' ' + str(A) + ' : ' + str(k) + ' ' + str(B) + ' ' + str(C) + ' ' + str(prob)


    
