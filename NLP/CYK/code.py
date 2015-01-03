## given a set of CNF rules with prob , and a tagged sent
## gives the cyk tree
## rules input - S -> NP VP = 1.0
## sent The_DET man_NN saw_VB the_DET girl_NN ._SYM

import cyk

#f = open('rules_cnf.txt','r')
f = open('rules.txt','r')
text = f.readlines()
f.close()

rules ={}
for t in text:
    t = t[:-1]
    r,p = t.split('=')
    rules[r.strip()] = p.strip()
   
#f = open('English_Test_Parse.txt','r')

f=open('text.txt','r')
text = f.readlines()
f.close()

sentences = []
for t in text:
    print t
    tag =[]
    tag.append('ROOT')
    t = t[:-1]
    t = t.split()
    for i in t:
	w,pos = i.split('_')
	tag.append(pos)
    sentences.append(tag)
    cyk.build_tree(tag,rules)
    


