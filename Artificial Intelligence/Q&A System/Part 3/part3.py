import nltk

query = raw_input("Enter bold words in round brackets (): " )

text = nltk.word_tokenize(query)

pos = nltk.pos_tag(text)
ques = ""
player = ""
matchno = ""

act = query.split("(")
acti = act[1].split(")")
action = acti[0]
print pos
for i in range(len(pos)):
    if pos[i][1] == "WRB" or pos[i][1]=="WP" or pos[i][1] == "WDT":
	ques = pos[i][0]
	if pos[i+1][1] == "NN" or pos[i+1][1] =="NNS":
	    print pos[i+1]
	    if pos[i+1][0] != "(":
	    	ques+= " " + str(pos[i+1][0])
	    	i = i+1
	elif pos[i+3][1] == "NN" or pos[i+3][1] =="NNS":
	    if pos[i+3][0] != "(":
	    	ques+= " " + str(pos[i+3][0])
	    	i = i+3
    elif pos[i][1] == "NNP" and pos[i][0] != "(" and pos[i][0] != ")":
	player = pos[i][0]
    elif pos[i][1] == "VBD" or pos[i][1] == "VBN":
	if pos[i][0]!="was" and pos[i][0]!=action and pos[i][0] != "were":
		print "this is me"
		print pos[i][0],i
		action += " " + pos[i][0]
    elif pos[i][0] == "match":
	if pos[i-1][1] == "JJ":
	    matchno = pos[i-1][0]
	elif pos[i+1][1] == "CD":
	    matchno = pos[i+1][0]
print ques
print player
print action
print matchno

