from nltk import load_parser
#parser = load_parser('simple-sem.fcfg',trace=0)
s=raw_input()
s=s.split(',')
noun = s[0].split(' ')[2]
quant = s[0].split(noun)[0]
tokens = []
quant = quant.strip(' ')
print noun
print quant
tokens.append(quant)
tokens.append(noun)
l=s[1]
if l.find("and") != -1:
    p=l.split("and")
    p[0] = p[0][1:-1] 
    p[1] = p[1][1:-1]
    tokens.append(p[0])
    tokens.append(p[1])
if l.find("is given to")!= -1:
    p=l.split("is given to")
    p[0] = p[0][1:-1] 
    p[1] = p[1][1:-1]
    tokens.append(p[0])
    tokens.append(p[1])
if l.find("consists of")!= -1:
    p=l.split("consists of")
    p[0] = p[0][1:-1] 
    p[1] = p[1][1:-1]
    tokens.append(p[0])
    tokens.append(p[1])
if l.find("contains")!=-1:
    p=l.split("contains")
    p[0] = p[0][1:-1] 
    p[1] = p[1][1:-1]
    tokens.append(p[0])
    tokens.append(p[1])
if l.find("if")!=-1 and l.find("then")!=-1:
    p=l.split("if")
    p=p[1].split("then")
    p[0] = p[0][1:-1] 
    p[1] = p[1][1:]
    tokens.append(p[0])
    tokens.append(p[1])

print tokens
d = {}
d['player']='player(x)'
d['matches'] = "match(x)"
d['player of match '] = 'pom(x,y)'
d['player of winning '] = 'pow(x,y)'
d['losing side']='lose(x,y)'
d['ducks']='duck(x,y)'
d['innings'] = 'inning(x)'
d['strike rate of player is above 200.0']='strikerate(x,y,200)'
d['more sixes than fours']='sixfour(x,y)'
d['boundary']='boundary(x,y)'
d['strike rate was below 100']='strikerate(x,y,100)'
d['50 runs in batting']='score50(x,y)'
d['at least 1 wicket']='wicket1(x,y)'
d['bowled  more  than 7 overs']='bowl7(x,y)'
d['failed to get any wicket']='nowicket(x,y)'
d['did  not  claim  any  wicket']='nowicket(x,y)'
d['more than 8 runs per over']='runs8(x,y)'
d['scored hundred']='runs100(x,y)'
d['team lost']='lose(x,y)'
d['less  than  26  years old']='age26(x)'
d['more than 250']='runs250(x,y)'


#lkeys=d.keys()
flag=0
p=""

if tokens[2].find("player")!=-1:
	t='exists y.player(y) and '
	flag=1
if tokens[2].find("side")!=-1:
	t='exists y.team(y) and '
	flag=2
if tokens[2].find("match")!=-1:
	t='for all y.match(y) and '
	flag=3
if tokens[2].find("bowler")!=-1:
	t='exists y.bowler(y) and '
	flag=4
if tokens[2].find("batsm")!=-1:
	t='exists y.batsman(y) and '
	flag=5
for i in d:
	if tokens[2].find(i)!=-1:
		if flag==1 and i=="player":
			h=""
		elif flag==3 and i=="matches":
			h=""
		else:
			p=d[i]



for i in d:
	if i=="ducks":
		d["ducks"]
	if tokens[3].find(i)!=-1:
		q=d[i]


if 'For all' in tokens:
	query = 'all x.('
	for i in d:
		if tokens[1].find(i)!=-1:
			query =query +d[i]
	query= query +' and '+t+p+' -> '+q+')'
elif 'There exists' in tokens:
	query = 'exists x.('
	for i in d:
		if tokens[1].find(i)!=-1:
			query=query + d[i]
	query=query+ 'and' +t+p+' and ' +q +')'
print query
