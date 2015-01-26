from collections import Counter

def em_func(file1):
 f = open(file1,'r')
 tagset = ['NN','NST','NNP','PRP','DEM','VM','VAUX','JJ','RB','PSP','RP','CC','WQ','QF','QC','QO','CL','INTF','INJ','NEG','UT','SYM','XC','RDP','ECH','UNK','START','END']

 text = f.readlines()

 word = []
 tag = []
 list1 = []

 prob_list = []


 for t in text:
    t = t.split()
    sent = t[2:-1]
    for i in sent:
	i = i.split('_')
	word.append(i[0])
	tag.append(i[1])
	list1.append([i[0],i[1]])

 
 
 w = Counter(word)
 w = w.most_common()
 new_word = [] 
 count = 0
 for i,j in w:
    count += 1
    new_word.append(i)
    tagged = []
    for k,l in list1:
	if k==i:
	    tagged.append(l)
    tagged_c = Counter(tagged)
    tagged_c = tagged_c.most_common()
    for u,v in tagged_c:
	prob_list.append([i,u,v/float(j)])

 emission_matrix = [[0]*len(tagset) for _ in range(count)]
 trylist = []
 for i,j,k in prob_list:
     #print i,
    trylist.append(new_word.index(i))
    #print tagset.index(j)
    emission_matrix[new_word.index(i)][tagset.index(j)] = k
    #print j, 
    #print tagset.index(j)
 #print max(trylist)
 #print count

 return emission_matrix,new_word

	


    
   
