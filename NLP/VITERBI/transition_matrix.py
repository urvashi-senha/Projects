from collections import Counter
from itertools import tee, islice
def ngrams(lst, n):
     tlst = lst
     while True:
            a, b = tee(tlst)
            l = tuple(islice(a, n))
            if len(l) == n:
                     yield l
                     next(b)
                     tlst = b
            else:
		break


def tr_func(file1):
 f = open(file1,'r')

 tag = []
 tagset = ['NN','NST','NNP','PRP','DEM','VM','VAUX','JJ','RB','PSP','RP','CC','WQ','QF','QC','QO','CL','INTF','INJ','NEG','UT','SYM','XC','RDP','ECH','UNK','START','END']


 trans_matrix = [[0]*len(tagset) for _ in range(len(tagset))]

 text = f.readlines()
 for t in text:
    t = t.split()
    sent = t[2:-1]
    for i in range(len(sent)):
	sent[i] = sent[i].split('_')
	if i==0:
	    tag.append('START')
	tag.append(sent[i][1])
	if i==len(sent)-1:
	    tag.append('END')

 tag_c = Counter(tag)
 tag_c = tag_c.most_common()

 tag_bi = Counter(ngrams(tag,2))
 tag_bi = tag_bi.most_common()


 for i, j in tag_bi:
    for k, l in tag_c:
	if k==i[0]:
	    p = j/float(l)
	    row = int(tagset.index(i[0]))
	    col = int(tagset.index(i[1])) 
	    trans_matrix[row][col] = p



 #for i in range(28):
 #   for j in range(28):
 #	print trans_matrix[i][j],
 #   print ''
 return trans_matrix








