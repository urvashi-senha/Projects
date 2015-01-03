import nltk	

def make(v,query,parse,dt):
	l = nltk.LogicParser()
	
	var =  """ 
	India => i
	New Zealand=> n
	Match1 => m1
	Match2 => m2
	Match3 => m3
	team => {i,n}
	match => {m1,m2,m3}
	pomteam => {(m1,i),(m2,n),(m3,i)}
	winteam => {(m1,i),(m2,n),(m3,i)}
	"""

	val = nltk.parse_valuation(v)
	#print val
	
	dom=val.domain
	m = nltk.Model(dom , val)
	dom=m.domain
	#print dom
	g = nltk.Assignment(dom,[])
	#print g	
	print "************************"
	#print m.evaluate('all x.( (match(x) & exists y.(team(y) and (pomteam(x,y) and  winteam(x,y)))) | (-match(x)) )', g)
	print m.evaluate(query, g)
	print "************************"

	fmla1 = l.parse(parse)
	varnames = m.satisfiers(fmla1, 'x' ,g)
	for i in varnames:
	    for p,q in dt.iteritems():
		if q == i:
		    print p


