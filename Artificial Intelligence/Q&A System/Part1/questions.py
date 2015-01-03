import re
def player1_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines):
	ans = []	
	bowler=[]
	if maxim == 1 or noof!= '0':
		maxi = 0
		count = 0
		player1 = None
		maxplayer1 = {}

	for i in range(len(lines)):
		if player2 != None and player1 == None:
			searc = "to "+player2
		elif player1!=None and player2 == None:
			searc = player1 + " to"
		elif player1!=None and player2!=None:
			searc = player1+" to "+player2
		if re.search(searc,lines[i]):
			#print lines[i]
			if(re.search(score,lines[i+1])):
				if maxim == 0 and noof == '0':
					b = lines[i].split('to')[0]
					if b not in bowler:
						bowler.append(b)
				elif maxim == 1 or noof!='0' :
					if player1 == None:
						player1 = lines[i].split('to')[0]
						count = count+1
						maxplayer1[player1]=count
						#print "Count:" + str(count)
					else:
						if(lines[i].split('to')[0] == player1):
							count = count + 1
							#print "Count:" + str(count)
							maxplayer1[player1]=count
						else:
						    	#print player1
							maxplayer1[player1] = count
							if count > maxi:
								maxi = count
							player1 = lines[i].split('to')[0]
							count = 1
							maxplayer1[player1]=count
	if maxim == 1 or noof!= '0':
	    #print maxplayer1
		if maxim==0 and noof!='0':
		     maxi = str(noof)
		for i in maxplayer1:
			if str(maxplayer1[i]) == str(maxi):
			    	if i not in ans:
					ans.append(i)
	elif maxim==0 and noof == '0':
	    	if bowler not in ans:
			ans.append(bowler)
	return ans


def player2_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines):
	ans = []
	batsmen = []
	if maxim == 1 or noof!='0' :
		maxi = 0
		count = 0
		player2 = None
		maxplayer2 = {}

	for i in range(len(lines)):
		if player2 != None and player1 == None:
			searc = "to "+player2
		elif player1!=None and player2 == None:
			searc = player1 + " to"
		elif player!=None and player2!=None:
			searc = player1+" to "+player2
		if re.search(searc,lines[i]):
		    #print lines[i]
			if maxim == 0 and noof=='0':
				if(re.search(score,lines[i+1])):
					b = lines[i].split('to')[0]
					if b not in batsmen:
						batsmen.append(b)
			elif maxim == 1 or noof!='0':
				if player2 == None:
					player2 = lines[i].split('to')[1]
					count = count+1
					maxplayer2[player2]=count
					#print "Count:" + str(count)
				else:
					if(lines[i].split('to')[1] == player2):
						count = count + 1
						#print "Count:" + str(count)
						maxplayer2[player2]=count
					else:
					    #print player2
						maxplayer2[player2] = count
						if count > maxi:
							maxi = count
						player2 = lines[i].split('to')[1]
						count = 1
						maxplayer2[player2]=count
	if maxim == 1 or noof!='0':
	    #print maxplayer2
		if maxim==0 and noof!='0':
		     maxi = str(noof)
		for i in maxplayer2:
			if str(maxplayer2[i]) == maxi:
			    	if i not in ans:
					ans.append(i)
	elif maxim == 0 and noof=='0':
			    	if batsmen not in ans:
					ans.append(batsmen)
	
	return ans
def over_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines):
	ans = []	
	over = []
	score = str(score)
	if maxim == 1 or noof!= '0':
		maxi = 0
		count = 0
		over = None
		maxover = {}
	for i in range(len(lines)):
		if player2 != None and player1 == None:
			searc = "to "+player2
		elif player1!=None and player2 == None:
			searc = player1 + " to"
		elif player1!=None and player2!=None:
			searc = player1+" to "+player2

		if re.search(searc,lines[i]):
		    #print lines[i]
			if(re.search(score,lines[i+1])):
				if maxim == 0 and noof=='0':
					over.append(lines[i-1].split('.')[0])
				elif maxim == 1  or noof!='0':
					if over == None:
						over = lines[i-1].split('.')[0]
						count = count+1
						maxover[over]=count
		#				print "Count:" + str(count)
					else:
						if(lines[i-1].split('.')[0] == over):
							count = count + 1
		#					print "Count:" + str(count)
							maxover[over]=count
						else:
							maxover[over] = count
							if count > maxi:
								maxi = count
							over = lines[i-1].split('.')[0]
							count = 1
							maxover[over]=count
	if maxim == 1 or noof!='0':
	    #   print maxover
		if maxim==0 and noof!='0':
		     maxi = noof
	#	     print maxi
		for i in maxover:
		    #		print maxover[i]
			if str(maxover[i]) == str(maxi):
				ans.append(i)
			return ans
	elif maxim == 0 and noof=='0':
		return over

def ball_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines):
	ball = []
	if player2 != None and player1 == None:
		searc = "to "+player2
	elif player1!=None and player2 == None:
		searc = player1 + " to"
	elif player!=None and player2!=None:
		searc = player1+" to "+player2
	for i in range(len(lines)):
		if re.search(searc,lines[i]):
		    #	print lines[i]
			if(re.search(score,lines[i+1])):
				over = lines[i-1].split('.')[0]
				if over == overno:
					ball.append(lines[i-1].split('.')[1])
	return ball


