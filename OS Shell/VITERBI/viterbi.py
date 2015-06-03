import emission_matrix as em
import transition_matrix as tr
import sys

file1 = sys.argv[1] # testfile
file2 = sys.argv[2] # training file

f = open(file1,'r')
text = f.readlines()
tagset = ['NN','NST','NNP','PRP','DEM','VM','VAUX','JJ','RB','PSP','RP','CC','WQ','QF','QC','QO','CL','INTF','INJ','NEG','UT','SYM','XC','RDP','ECH','UNK','START','END']
replaceword = 'hinxI'
em_mat,new_word = em.em_func(file2) 
tr_mat = tr.tr_func(file2)

#print em_mat
#print tr_mat

for t in text:
 viterbi = []
 backpointer = []
 word = []
 t = t[:-1]
 t = t.split()

 sent = t[2:-2]
 for i in sent:
	 #i = i.split('_')
	 word.append(i)
	 


 sent_len = len(word)

########## FIRST WORD ################

 first_viterbi = {}
 first_backpointer = {}

 for tag in tagset:
    if tag!='START':
        if word[0] in new_word:
		first_viterbi[tag] = tr_mat[tagset.index('START')][tagset.index(tag)] * em_mat[new_word.index(word[0])][tagset.index(tag)]
	else:
		first_viterbi[tag] = tr_mat[tagset.index('START')][tagset.index(tag)] * em_mat[new_word.index(replaceword)][tagset.index(tag)]
		
	first_backpointer[tag] = 'START'
	
 viterbi.append(first_viterbi)
 backpointer.append(first_backpointer)


############################################


###########3 OTHER WORDS ###################


 for i in range(1,sent_len):
    this_viterbi = {}
    this_backpointer= {}
    prev_viterbi = viterbi[-1]
    if word[i] not in new_word:
	nw = replaceword
    else:
	nw = word[i]
    for tag in tagset:
	if tag!='START':
	    best_prev = None
	    best_prob = 0.0
	    for prev_tag in prev_viterbi.keys():
		prob = prev_viterbi[prev_tag] * tr_mat[tagset.index(tag)][tagset.index(prev_tag)] * em_mat[new_word.index(nw)][tagset.index(tag)]
		if prob >= best_prob:
		    best_prev = prev_tag
		    best_prob = prob

	    this_viterbi[tag] = prev_viterbi[best_prev] * tr_mat[tagset.index(tag)][tagset.index(best_prev)] * em_mat[new_word.index(nw)][tagset.index(tag)]
	    this_backpointer[tag] = best_prev
    viterbi.append(this_viterbi)
    backpointer.append(this_backpointer)



############################################



################ LAST TAG ###################

 prev_viterbi = viterbi[-1]

 best_prev = None
 best_prob = 0.0
 for prev_tag in prev_viterbi.keys():
		prob = prev_viterbi[prev_tag] * tr_mat[tagset.index(prev_tag)][tagset.index('END')]
		if prob >= best_prob:
		    best_prev = prev_tag
		    best_prob = prob
 prob_tagseq = prev_viterbi[best_prev] * tr_mat[tagset.index('END')][tagset.index(best_prev)]
 best_tagseq = [ 'END', best_prev ]

 backpointer.reverse()

 current_best_tag = best_prev

 for bp in backpointer:
    best_tagseq.append(bp[current_best_tag])
    current_best_tag = bp[current_best_tag]

 best_tagseq.reverse()


 for i in range(sent_len):
	print word[i] + '_' + best_tagseq[i+1] + ' ',
 print ''
#print best_tagseq















