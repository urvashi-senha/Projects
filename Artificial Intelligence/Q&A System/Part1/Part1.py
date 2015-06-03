import re
import os
import questions

player1=None
player2=None
noof='0'
score='0'
maxim=0
overno=None
question=None
d = []
def finds(s,t):
    return s.find(t)

def matchs(s):
	if(finds(s,'first')!=-1):
		return "first"
	elif(finds(s,'second')!=-1):
		return "second"
	elif(finds(s,'third')!=-1):
		return "third"
	elif(finds(s,'fourth')!=-1):
		return "fourth"
	elif(finds(s,'fifth')!=-1):
		return "fifth"
def splits(s):
	if(finds(s,"of which")!=-1):
		return s.split("of which")
	elif(finds(s,"in which")!=-1):
		return s.split("in which")
	elif(finds(s,"who")!=-1):
		return s.split("who")

def ques(s):
	if finds(s,"ball")!=-1:
		return "ball"
	elif finds(s,"over")!=-1:
		return "over"
	elif finds(s,"dismissed")!=-1:
		return "player1"
	elif finds(s,"hit")!=-1:
		return "player2"
	elif finds(s,"bowler")!=-1:
		return "player1"

def play(s):
    	player1 = None
	player2 = None
	if((finds(s,"hit"))!=-1):
		l=s.split("hit")
		player2=l[0].lstrip()
		player2=player2.rstrip()
	elif((finds(s,"bowl"))!=-1):
		l=s.split("bowl")
		player1=l[0].lstrip()
		player1=player1.rstrip()
	elif((finds(s,"was out"))!=-1):
		l=s.split("was")
		player2=l[0].lstrip()
		player2=player2.rstrip()
	return l,player1,player2

def overs(s):
	if len(s)>=2:
		t=s[1].lstrip()
		if(t[0]!='s'):
			q=t.split(' ')
			return q[0].rstrip(',')

def scores(s):
	l=re.findall("\d+",s)
	if len(l)>0:
		noof=l[0]
		w=s.rstrip()
		score=w.split(' ')[-1].rstrip(',')
		if score.find("six")!=-1:
			return "six"
		elif score.find("four")!=-1:
			return "four"
		elif score.find("wide")!=-1:
			return "wide"
	
	elif ((s.find("max"))!=-1):
		maxim=1
		w=s.rstrip()
		score=w.split(' ')[-1].rstrip(',')
		if score.find("six")!=-1:
			return "six"
		elif score.find("four")!=-1:
			return "four"
		elif score.find("wide")!=-1:
			return "wide"
	else:
		w=s.rstrip()
		score=w.split(' ')[-1].rstrip(',')
		if score.find("six")!=-1:
			return "six"
		elif score.find("four")!=-1:
			return "four"
		elif score.find("wide")!=-1:
			return "wide"
def print_ans(ans):
        answ = []
	for i in ans:
	    if  i not in answ:
		answ.append(i)
	print answ

def main():
	a=raw_input("Enter the Question\n")
	b=a.split("match,")
	matchno = matchs(b[0])
	d = splits(b[1])
	question = ques(d[1])
	l,player1,player2 = play(d[0])
	p=l[1].split("in over")
	overno = overs(p)
	score = scores(p[0])
	
	#print "Match "+str(matchno)
	#print "Player1 "+str(player1)
	#print "Player2 "+str(player2)
	#print "Score "+str(score)
	#print "OverNo "+str(overno)
	#print maxim
	#print "Question "+str(question)
	#print "Noof "+str(noof)
	os.chdir("../")
	if matchno == "first":
		lines = open('dataset/match1.txt','r').readlines()
	if matchno == "second":
		lines = open('dataset/match2.txt','r').readlines()
	if matchno == "third":
		lines = open('dataset/match3.txt','r').readlines()
	if matchno == "fourth":
		lines = open('dataset/match4.txt','r').readlines()
	if matchno == "fifth":
		lines = open('dataset/match5.txt','r').readlines()
	if question == "player1":
		ans = questions.player1_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines)
		print_ans(ans)
	elif question == "player2":
		ans = questions.player2_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines)
		print_ans(ans)
	elif question == "over":
		ans  = questions.over_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines)
		print_ans(ans)
		#print ans
	elif question == "ball":
		ans = questions.ball_ques(matchno,player1,player2,maxim,noof,score,overno,question,lines)
		print_ans(ans)


	

#if __name__ == " __main__":
main()
