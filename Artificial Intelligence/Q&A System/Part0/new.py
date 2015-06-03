#--------- query 1 ---------------#

def query1_parse(info1,info2,info3,info4,info5):
    winner1 = str(info1[0][:-1]).split()
    player1 = str(info1[1][:-1]).split('(')
    play1 = player1[1]
    win1 = winner1[0]
    if(win1 == 'New'):
	win1 = 'New Zealand'
    elif(win1 == 'Match'):
	win1 = play1
    
    winner2 = str(info2[0][:-1]).split()
    player2 = str(info1[1][:-1]).split('(')
    play2 = player2[1]
    win2 = winner2[0]
    if(win2 == 'New'):
	win2 = 'New Zealand'
    elif(win2 == 'Match'):
	win2 = play2

    winner3 = str(info3[0][:-1]).split()
    player3 = str(info3[1][:-1]).split('(')
    play3 = player3[1]
    win3 = winner3[0]
    if(win3 == 'New'):
	win3 = 'New Zealand'
    elif(win3 == 'Match'):
	win3 = play3
    winner4 = str(info4[0][:-1]).split()
    player4 = str(info4[1][:-1]).split('(')
    play4 = player4[1]
    win4 = winner4[0]
    if(win4 == 'New'):
	win4 = 'New Zealand'
    elif(win4 == 'Match'):
	win4 = play4
    winner5 = str(info5[0][:-1]).split()
    player5 = str(info5[1][:-1]).split('(')
    play5 = player5[1]
    win5 = winner5[0]
    if(win5 == 'New'):
	win5 = 'New Zealand'
    elif(win5 == 'Match'):
	win5 = play5
    dict1 = {}
    dict1['m1'] = win1
    dict1['m2'] = win2
    dict1['m3'] = win3
    dict1['m4'] = win4
    dict1['m5'] = win5

    dict2 = {}
    dict2['m1'] = play1
    dict2['m2'] = play2
    dict2['m3'] = play3
    dict2['m4'] = play4
    dict2['m5'] = play5

    return dict1,dict2



#----------- query 2 -----------------#

def query2_parse(info1,info2,info3,info4,info5,bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10):

    winner1 = str(info1[0][:-1]).split()
    player1 = str(info1[1][:-1]).split('(')
    play1 = player1[1]
    win1 = winner1[0]

    if(play1 == 'New'):
	play1 = 'India'
    elif(play1 == 'India'):
	play1 = 'New Zealand'
    if(win1 == 'New'):
	win1 = 'India'
    elif(win1 == 'India'):
	win1 = 'New Zealand'
    elif(win1 == 'Match'):
	win1 = play1
    
    winner2 = str(info2[0][:-1]).split()
    player2 = str(info1[1][:-1]).split('(')
    play2 = player2[1]
    win2 = winner2[0]
    if(play2 == 'New'):
	play2 = 'India'
    elif(play2 == 'India'):
	play2 = 'New Zealand'
    if(win2 == 'New'):
	win2 = 'India'
    elif(win2 == 'India'):
	win2 = 'New Zealand'
    elif(win2 == 'Match'):
	win2 = play2

    winner3 = str(info3[0][:-1]).split()
    player3 = str(info3[1][:-1]).split('(')
    play3 = player3[1]
    win3 = winner3[0]
    if(play3 == 'New'):
	play3 = 'India'
    elif(play3 == 'India'):
	play3 = 'New Zealand'
 
    if(win3 == 'New'):
	win3 = 'India'
    elif(win3 == 'India'):
	win3 = 'New Zealand'
    elif(win3 == 'Match'):
	win3 = play3
    
    winner4 = str(info4[0][:-1]).split()
    player4 = str(info4[1][:-1]).split('(')
    play4 = player4[1]
    win4 = winner4[0]
    if(play4 == 'New'):
	play4 = 'India'
    elif(play4 == 'India'):
	play4 = 'New Zealand'
    if(win4 == 'New'):
	win4 = 'India'
    elif(win4 == 'India'):
	win4 = 'New Zealand'
    elif(win4 == 'Match'):
	win4 = play4
    
    winner5 = str(info5[0][:-1]).split()
    player5 = str(info5[1][:-1]).split('(')
    play5 = player5[1]
    win5 = winner5[0]
    if(play5 == 'New'):
	play5 = 'India'
    elif(play5 == 'India'):
	play5 = 'New Zealand'
    if(win5 == 'New'):
	win5 = 'India'
    elif(win5 == 'India'):
	win5 = 'New Zealand'
    elif(win5 == 'Match'):
	win5 = play5
    
    dict1 = {}
    dict1['m1'] = win1
    dict1['m2'] = win2
    dict1['m3'] = win3
    dict1['m4'] = win4
    dict1['m5'] = win5

    inn1 = str(info1[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info1[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
    if win1 == inn1:
    	inn = 1
    else:
	inn = 2
    
    if(inn == 1):
    	dict2 = {}
    	for i in bat1:
		temp = bat1[i]
		if(int(temp[1]) == 0):
	    		dict2['m1'] = inn1
    elif(inn==2):
    	dict2 = {}
    	for i in bat2:
		temp = bat2[i]
		if(int(temp[1]) == 0):
	    		dict2['m1'] = inn2


    inn1 = str(info2[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info2[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
    if(win2 == inn1):
    	inn = 1
    else:
	inn = 2
    
    if(inn == 1):
    	for i in bat3:
		temp = bat3[i]
		if(int(temp[1]) == 0):
	    		dict2['m2'] = inn1
    elif(inn==2):
    	for i in bat4:
		temp = bat4[i]
		if(int(temp[1]) == 0):
	    		dict2['m2'] = inn2



    inn1 = str(info3[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info3[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
    if(win3 == inn1):
    	inn = 1
    else:
	inn = 2
    
    if(inn == 1):
    	for i in bat5:
		temp = bat5[i]
		if(int(temp[1]) == 0):
	    		dict2['m3'] = inn1
    elif(inn==2):
    	for i in bat6:
		temp = bat6[i]
		if(int(temp[1]) == 0):
	    		dict2['m3'] = inn2



    inn1 = str(info4[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info4[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
    if(win4 == inn1):
    	inn = 1
    else:
	inn = 2
    
    if(inn == 1):
    	for i in bat7:
		temp = bat7[i]
		if(int(temp[1]) == 0):
	    		dict2['m4'] = inn1
    elif(inn==2):
    	for i in bat8:
		temp = bat8[i]
		if(int(temp[1]) == 0):
	    		dict2['m4'] = inn2

    inn1 = str(info5[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info5[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
    if(win5 == inn1):
    	inn = 1
    else:
	inn = 2
    
    if(inn == 1):
    	for i in bat9:
		temp = bat9[i]
		if(int(temp[1]) == 0):
	    		dict2['m5'] = inn1
    elif(inn==2):
    	for i in bat10:
		temp = bat10[i]
		if(int(temp[1]) == 0):
	    		dict2['m5'] = inn2

    return dict1,dict2

#-----------query 3------------#
def query3_parse(info1,info2,info3,info4,info5,info6,info7,info8,info9,info10):
	dict1={}
	dict2={}
	lis1=[] 
	lis2=[]
	lis3=[]
	lis4=[]
	lis5=[]
	lis6=[]
	lis7=[]
	lis8=[]
	lis9=[]
	lis10=[]
	lis11=[]
	lis12=[]
	lis13=[]
	lis14=[]
	lis15=[]
	lis16=[]
	lis17=[]
	lis18=[]
	lis19=[]
	lis20=[]
	
	for k in info1:
		p=info1[k]
		if float(p[6])>200:
			lis1.append(k)
		if int(p[5])>int(p[4]):
			lis11.append(k)
	for i in info2.keys():
		if float(info2.get(i)[-1])>200:
			lis2.append(i)
		if int(info2.get(i)[5])>int(info2.get(i)[4]):
			lis12.append(i)
	for i in info3.keys():
		if float(info3.get(i)[-1])>200:
			lis3.append(i)
		if int(info3.get(i)[5])>int(info3.get(i)[4]):
			lis13.append(i)
	for i in info4.keys():
		if float(info4.get(i)[-1])>200:
			lis4.append(i)
		if int(info4.get(i)[5])>int(info4.get(i)[4]):
			lis14.append(i)
	for i in info5.keys():
		if float(info5.get(i)[-1])>200:
			lis5.append(i)
		if int(info5.get(i)[5])>int(info5.get(i)[4]):
			lis15.append(i)
	for i in info6.keys():
		if float(info6.get(i)[-1])>200:
			lis6.append(i)
		if int(info6.get(i)[5])>int(info6.get(i)[4]):
			lis16.append(i)
	for i in info7.keys():
		if float(info7.get(i)[-1])>200:
			lis7.append(i)
		if int(info7.get(i)[5])>int(info7.get(i)[4]):
			lis17.append(i)
	for i in info8.keys():
		if float(info8.get(i)[-1])>200:
			lis8.append(i)
		if int(info8.get(i)[5])>int(info8.get(i)[4]):
			lis18.append(i)
	for i in info9.keys():
		if float(info9.get(i)[-1])>200:
			lis9.append(i)
		if int(info9.get(i)[5])>int(info9.get(i)[4]):
			lis19.append(i)
	for i in info10.keys():
		if float(info10.get(i)[-1])>200:
			lis10.append(i)
		if int(info10.get(i)[5])>int(info10.get(i)[4]):
			lis20.append(i)
	dict1['in1']=lis1
	dict1['in3']=lis2
	dict1['in5']=lis3
	dict1['in7']=lis4
	dict1['in9']=lis5
	dict1['in2']=lis6
	dict1['in4']=lis7
	dict1['in6']=lis8
	dict1['in8']=lis9
	dict1['in10']=lis10
	dict2['in1']=lis11
	dict2['in3']=lis12
	dict2['in5']=lis13
	dict2['in7']=lis14
	dict2['in9']=lis15
	dict2['in2']=lis16
	dict2['in4']=lis17
	dict2['in6']=lis18
	dict2['in8']=lis19
	dict2['in10']=lis20
	
	return dict1,dict2

#------ query4 --------#
def query4_parse(bat1,bat2,bat3,bat4,bat5):
	dict1 = {}
	dict2 = {}
	keys = bat1.keys()
	list1 = []
	for key in keys:
		four = bat1.get(key).split(',')[-3]
		if four >= 1:
			list1.append(bat1.get(key).split(',')[0])
	dict1['m1'] = list1

	keys = bat2.keys()
	list2 = []
	for key in keys:
		four = bat2.get(key).split(',')[-3]
		if four >= 1:
			list2.append(bat2.get(key).split(',')[0])
	dict1['m2'] = list2

	keys = bat3.keys()
	list3 = []
	for key in keys:
		four = bat3.get(key).split(',')[-3]
		if four >= 1:
			list3.append(bat3.get(key).split(',')[0])
	dict1['m3'] = list3

	keys = bat4.keys()
	list4 = []
	for key in keys:
		four = bat4.get(key).split(',')[-3]
		if four >= 1:
			list4.append(bat4.get(key).split(',')[0])
	dict1['m4'] = list4

	keys = bat5.keys()
	list5 = []
	for key in keys:
		four = bat5.get(key).split(',')[-3]
		if four >= 1:
			list5.append(bat5.get(key).split(',')[0])
	dict1['m5'] = list5


	keys = bat1.keys()
	list1 = []
	for key in keys:
		strk = bat1.get(key).split(',')[-1]
		if float(strk) < 100:
			list1.append(bat1.get(key).split(',')[0])
	dict2['m1'] = list1

	keys = bat2.keys()
	list2 = []
	for key in keys:
		strk = bat2.get(key).split(',')[-1]
		if float(strk) < 100:
			list2.append(bat2.get(key).split(',')[0])
	dict2['m2'] = list2

	keys = bat3.keys()
	list3 = []
	for key in keys:
		strk = bat3.get(key).split(',')[-1]
		if float(strk)< 100:
			list3.append(bat3.get(key).split(',')[0])
	dict2['m3'] = list3

	keys = bat4.keys()
	list4 = []
	for key in keys:
		strk = bat4.get(key).split(',')[-1]
		if float(strk) < 100:
			list4.append(bat4.get(key).split(',')[0])
	dict2['m4'] = list4

	keys = bat5.keys()
	list5 = []
	for key in keys:
		strk = bat5.get(key).split(',')[-1]
		if float(strk)< 100:
			list5.append(bat5.get(key).split(',')[0])
	dict2['m5'] = list5


	return dict1,dict2

#----------- query 5 -----------------#
def query5_parse(bat1,bat2,bat3,bat4,bat5,bowl1,bowl2,bowl3,bowl4,bowl5):
    	dict1 = {}
	list1 = []
    	for i in bat1:
		temp = bat1[i]
		if(int(temp[1]) > 50):
	    		list1.append(i)
	dict1['m1'] = list1
	list1 = []
    	for i in bat2:
		temp = bat2[i]
		if(int(temp[1])  > 50):
	    		list1.append(i)
	dict1['m2'] = list1
	list1 = []
    	for i in bat3:
		temp = bat3[i]
		if(int(temp[1]) > 50):
	    		list1.append(i)
	dict1['m3'] = list1
	list1 = []
    	for i in bat4:
		temp = bat4[i]
		if(int(temp[1]) > 50):
	    		list1.append(i)
	dict1['m4'] = list1
	list1 = []
    	for i in bat5:
		temp = bat5[i]
		if(int(temp[1]) > 50):
	    		list1.append(i)
	dict1['m5'] = list1
    	
	dict2 = {}
	list1 = []
	
    	for i in bowl1:
		temp = bowl1[i]
		if(int(temp[3]) > 0 ):
	    		list1.append(i)
	dict2['m1'] = list1
	list1 = []
    	for i in bowl2:
		temp = bowl2[i]
		if(int(temp[3]) > 0):
	    		list1.append(i)
	dict2['m2'] = list1
	list1 = []
    	for i in bowl3:
		temp = bowl3[i]
		if(int(temp[3]) > 0):
	    		list1.append(i)
	dict2['m3'] = list1
	list1 = []
    	for i in bowl4:
		temp = bowl4[i]
		if(int(temp[3]) > 0):
	    		list1.append(i)
	dict2['m4'] = list1
	list1 = []
    	for i in bowl5:
		temp = bowl5[i]
		if(int(temp[3]) > 0):
	    		list1.append(i)
	dict2['m5'] = list1
	return dict1,dict2

#---------------query 6------#
def query6_parse(bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10):
  
  bowlmorethan7={}
  nowicket={}
  for k,v in bowl1.iteritems():
	if float(v[0])>7:
		if 'm1' not in bowlmorethan7:		
			bowlmorethan7['m1']=[k]
		else: 
			bowlmorethan7['m1'].append(k)

  for k,v in bowl1.iteritems():
	if int(v[3])==0:
		if 'm1' not in nowicket:	 	
			nowicket['m1']=[k]
		else: 
			nowicket['m1'].append(k)
		
  for k,v in bowl2.iteritems():
	if float(v[0])>7:
		if 'm1' not in bowlmorethan7:		
			bowlmorethan7['m1']=[k]
		else: 
			bowlmorethan7['m1'].append(k)
  for k,v in bowl2.iteritems():
	if int(v[3])==0:
		if 'm1' not in nowicket:		
			nowicket['m1']=[k]
		else: 
			nowicket['m1'].append(k)
  for k,v in bowl3.iteritems():
	if float(v[0])>7:
		if 'm2' not in bowlmorethan7:		
			bowlmorethan7['m2']=[k]
		else: 
			bowlmorethan7['m2'].append(k)
  for k,v in bowl3.iteritems():
	if int(v[3])==0:
		if 'm2' not in nowicket:		
			nowicket['m2']=[k]
		else: 
			nowicket['m2'].append(k)
  for k,v in bowl4.iteritems():
	if float(v[0])>7:
		if 'm2' not in bowlmorethan7:		
			bowlmorethan7['m2']=[k]
		else: 
			bowlmorethan7['m2'].append(k)
  for k,v in bowl4.iteritems():
	if int(v[3])==0:
		if 'm2' not in nowicket:		
			nowicket['m2']=[k]
		else: 
			nowicket['m2'].append(k)
  for k,v in bowl5.iteritems():
	if float(v[0])>7:
		if 'm3' not in bowlmorethan7:		
			bowlmorethan7['m3']=[k]
		else: 
			bowlmorethan7['m3'].append(k)
  for k,v in bowl5.iteritems():
	if int(v[3])==0:
		if 'm3' not in nowicket:		
			nowicket['m3']=[k]
		else: 
			nowicket['m3'].append(k)
	
  for k,v in bowl6.iteritems():
	if float(v[0])>7:
		if 'm3' not in bowlmorethan7:		
			bowlmorethan7['m3']=[k]
		else: 
			bowlmorethan7['m3'].append(k)
  for k,v in bowl6.iteritems():
	if int(v[3])==0:
		if 'm3' not in nowicket:		
			nowicket['m3']=[k]
		else: 
			nowicket['m3'].append(k)
  for k,v in bowl7.iteritems():
	if float(v[0])>7:
		if 'm4' not in bowlmorethan7:		
			bowlmorethan7['m4']=[k]
		else: 
			bowlmorethan7['m4'].append(k)
  for k,v in bowl7.iteritems():
	if int(v[3])==0:
		if 'm4' not in nowicket:		
			nowicket['m4']=[k]
		else: 
			nowicket['m4'].append(k)
  for k,v in bowl8.iteritems():
	if float(v[0])>7:
		if 'm4' not in bowlmorethan7:		
			bowlmorethan7['m4']=[k]
		else: 
			bowlmorethan7['m4'].append(k)
  for k,v in bowl8.iteritems():
	if int(v[3])==0:
		if 'm4' not in nowicket:		
			nowicket['m4']=[k]
		else: 
			nowicket['m4'].append(k)
  for k,v in bowl9.iteritems():
	if float(v[0])>7:
		if 'm5' not in bowlmorethan7:		
			bowlmorethan7['m5']=[k]
		else: 
			bowlmorethan7['m5'].append(k)
  for k,v in bowl9.iteritems():
	if int(v[3])==0:
		if 'm5' not in nowicket:		
			nowicket['m5']=[k]
		else: 
			nowicket['m5'].append(k)
  for k,v in bowl10.iteritems():
	if float(v[0])>7:
		if 'm5' not in bowlmorethan7:		
			bowlmorethan7['m5']=[k]
		else: 
			bowlmorethan7['m5'].append(k)
  for k,v in bowl10.iteritems():
	if int(v[3])==0:
		if 'm5' not in nowicket:		
			nowicket['m5']=[k]
		else: 
			nowicket['m5'].append(k)
  return bowlmorethan7,nowicket

#-----query 7------#
def query7_parse(bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10):
	dict1 = {}
	dict2 = {}
	keys = bowl1.keys()
	list1 = []
	for key in keys:
		wicket = bowl1.get(key)[3]
		if int(wicket) == 0:
			list1.append(key)

	keys = bowl2.keys()
	list2 = []
	for key in keys:
		wicket = bowl2.get(key)[3]
		if int(wicket) == 0:
			list2.append(key)
	list1 = list1+list2
	dict1['m1'] = list1

	keys = bowl3.keys()
	list3 = []
	for key in keys:
		wicket = bowl3.get(key)[3]
		if int(wicket) == 0:
			list3.append(key)

	keys = bowl4.keys()
	list4 = []
	for key in keys:
		wicket = bowl4.get(key)[3]
		if int(wicket) == 0:
			list4.append(key)
	list3 = list3 + list4
	dict1['m2'] = list3

	keys = bowl5.keys()
	list5 = []
	for key in keys:
		wicket = bowl5.get(key)[3]
		if int(wicket) == 0:
			list5.append(key)

	keys = bowl6.keys()
	list6 = []
	for key in keys:
		wicket = bowl6.get(key)[3]
		if int(wicket) == 0:
			list6.append(key)
	list5 = list5 + list6
	dict1['m3'] = list5


	keys = bowl7.keys()
	list7 = []
	for key in keys:
		wicket = bowl7.get(key)[3]
		if int(wicket) == 0:
			list7.append(key)


	keys = bowl8.keys()
	list8 = []
	for key in keys:
		wicket = bowl8.get(key)[3]
		if int(wicket) == 0:
			list8.append(key)
	list7 = list7 + list8
	dict1['m4'] = list7

	keys = bowl9.keys()
	list9 = []
	for key in keys:
		wicket = bowl9.get(key)[3]
		if int(wicket) == 0:
			list9.append(key)

	keys = bowl10.keys()
	list10 = []
	for key in keys:
		wicket = bowl10.get(key)[3]
		if int(wicket) == 0:
			list10.append(key)
	list9 = list9 + list10
	dict1['m5'] = list9



	keys = bowl1.keys()
	list1 = []
	for key in keys:
		runs = bowl1.get(key)[4]
		if float(runs) > 8.00:
			list1.append(key)

	keys = bowl2.keys()
	list2 = []
	for key in keys:
		runs = bowl2.get(key)[4]
		if float(runs) > 8.00:
			list2.append(key)
	list1 = list1+list2
	dict2['m1'] = list1

	keys = bowl3.keys()
	list3 = []
	for key in keys:
		runs = bowl3.get(key)[4]
		if float(runs) > 8.00:
			list3.append(key)

	keys = bowl4.keys()
	list4 = []
	for key in keys:
		runs = bowl4.get(key)[4]
		if float(runs)> 8.00:
			list4.append(key)
	list3 = list3 + list4
	dict2['m2'] = list2

	keys = bowl5.keys()
	list5 = []
	for key in keys:
		runs = bowl5.get(key)[4]
		if float(runs) > 8.00:
			list5.append(key)

	keys = bowl6.keys()
	list6 = []
	for key in keys:
		runs = bowl6.get(key)[4]
		if float(runs) > 8.00:
			list6.append(key)
	list5 = list5 + list6
	dict2['m3'] = list5


	keys = bowl7.keys()
	list7 = []
	for key in keys:
		runs = bowl7.get(key)[4]
		if float(runs) >8.00:
			list7.append(key)


	keys = bowl8.keys()
	list8 = []
	for key in keys:
		runs = bowl8.get(key)[4]
		if float(runs) > 8.00:
			list8.append(key)
	list7 = list7 + list8
	dict2['m4'] = list7

	keys = bowl9.keys()
	list9 = []
	for key in keys:
		runs = bowl9.get(key)[4]
		if float(runs) > 8.00:
			list9.append(key)


	keys = bowl10.keys()
	list10 = []
	for key in keys:
		runs = bowl10.get(key)[4]
		if float(runs) > 8.00:
			list10.append(key)
	list9 = list9 + list10
	dict2['m5'] = list9


	return dict1,dict2

#---------------- query 8 -------------------#
def query8_parse(info1,info2,info3,info4,info5,bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10):
    
    inn1 = str(info1[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info1[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
   
    dict1 = {}
    list1 = []

    for i in bat1:
	temp = bat1[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn1);
    for i in bat2:
	temp = bat2[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn2);
    dict1['m1'] = list1


    inn1 = str(info2[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info2[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
   
    list1 = []

    for i in bat3:
	temp = bat3[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn1);
    for i in bat4:
	temp = bat4[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn2);

    dict1['m2'] = list1


    inn1 = str(info3[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info3[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
   
    list1 = []

    for i in bat5:
	temp = bat5[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn1);
    for i in bat6:
	temp = bat6[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn2);

    dict1['m3'] = list1

    inn1 = str(info4[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info4[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
   
    list1 = []

    for i in bat7:
	temp = bat7[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn1);
    for i in bat8:
	temp = bat8[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn2);

    dict1['m4'] = list1

    list1 = []

    inn1 = str(info5[2]).split()
    in1 = inn1[0]
    if in1 == 'New':
	inn1 = 'New Zealand'
    else:
	inn1 = 'India'
    inn2 = str(info5[3]).split()
    in2 = inn2[0]
    if in2 == 'New':
	inn2 = 'New Zealand'
    else:
	inn2 = 'India'
   
    list1 = []

    for i in bat9:
	temp = bat9[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn1);
    for i in bat10:
	temp = bat10[i]
	if(int(temp[1]) > 100):
	    	list1.append(inn2);
    dict1['m5'] = list1
    
    winner1 = str(info1[0][:-1]).split()
    player1 = str(info1[1][:-1]).split('(')
    play1 = player1[1]
    win1 = winner1[0]

    if(play1 == 'New'):
	play1 = 'India'
    elif(play1 == 'India'):
	play1 = 'New Zealand'
    if(win1 == 'New'):
	win1 = 'India'
    elif(win1 == 'India'):
	win1 = 'New Zealand'
    elif(win1 == 'Match'):
	win1 = play1
    
    winner2 = str(info2[0][:-1]).split()
    player2 = str(info1[1][:-1]).split('(')
    play2 = player2[1]
    win2 = winner2[0]
    if(play2 == 'New'):
	play2 = 'India'
    elif(play2 == 'India'):
	play2 = 'New Zealand'
    if(win2 == 'New'):
	win2 = 'India'
    elif(win2 == 'India'):
	win2 = 'New Zealand'
    elif(win2 == 'Match'):
	win2 = play2

    winner3 = str(info3[0][:-1]).split()
    player3 = str(info3[1][:-1]).split('(')
    play3 = player3[1]
    win3 = winner3[0]
    if(play3 == 'New'):
	play3 = 'India'
    elif(play3 == 'India'):
	play3 = 'New Zealand'
 
    if(win3 == 'New'):
	win3 = 'India'
    elif(win3 == 'India'):
	win3 = 'New Zealand'
    elif(win3 == 'Match'):
	win3 = play3
    
    winner4 = str(info4[0][:-1]).split()
    player4 = str(info4[1][:-1]).split('(')
    play4 = player4[1]
    win4 = winner4[0]
    if(play4 == 'New'):
	play4 = 'India'
    elif(play4 == 'India'):
	play4 = 'New Zealand'
    if(win4 == 'New'):
	win4 = 'India'
    elif(win4 == 'India'):
	win4 = 'New Zealand'
    elif(win4 == 'Match'):
	win4 = play4
    
    winner5 = str(info5[0][:-1]).split()
    player5 = str(info5[1][:-1]).split('(')
    play5 = player5[1]
    win5 = winner5[0]
    if(play5 == 'New'):
	play5 = 'India'
    elif(play5 == 'India'):
	play5 = 'New Zealand'
    if(win5 == 'New'):
	win5 = 'India'
    elif(win5 == 'India'):
	win5 = 'New Zealand'
    elif(win5 == 'Match'):
	win5 = play5
    
    dict2 = {}
    dict2['m1'] = win1
    dict2['m2'] = win2
    dict2['m3'] = win3
    dict2['m4'] = win4
    dict2['m5'] = win5

    return dict1,dict2

#----------------- query 9 ---------------#

def query9_parse(info,bowl1,bowl2,bowl3,bowl4,bowl5):

    dict1 = {}
    
    leftwickets = 0
    rightwickets = 0
    for i in bowl1:
	temp = bowl1[i]
	if( info[i] == 'Right'):
	    rightwickets += int(temp[3])
	elif( info[i] == 'Left'):
	    leftwickets += int(temp[3])
    if(rightwickets >= leftwickets):
   	dict1['m1'] = 'r'
    else:
       dict1['m1'] = 'l'
  


    leftwickets = 0
    rightwickets = 0
    for i in bowl2:
	temp = bowl2[i]
	if( info[i] == 'Right'):
	    rightwickets += int(temp[3])
	elif( info[i] == 'Left'):
	    leftwickets += int(temp[3])
    if(rightwickets >= leftwickets):
   	dict1['m2'] = 'r'
    else:
       dict1['m2'] = 'l'
  


    leftwickets = 0
    rightwickets = 0
    for i in bowl3:
	temp = bowl3[i]
	if( info[i] == 'Right'):
	    rightwickets += int(temp[3])
	elif( info[i] == 'Left'):
	    leftwickets += int(temp[3])
    if(rightwickets >= leftwickets):
   	dict1['m3'] = 'r'
    else:
       dict1['m3'] = 'l'


    leftwickets = 0
    rightwickets = 0
    for i in bowl4:
	temp = bowl4[i]
	if( info[i] == 'Right'):
	    rightwickets += int(temp[3])
	elif( info[i] == 'Left'):
	    leftwickets += int(temp[3])
    if(rightwickets >= leftwickets):
   	dict1['m4'] = 'r'
    else:
       dict1['m4'] = 'l'
   
    
    leftwickets = 0
    rightwickets = 0
    for i in bowl5:
	temp = bowl5[i]
	if( info[i] == 'Right'):
	    rightwickets += int(temp[3])
	elif( info[i] == 'Left'):
	    leftwickets += int(temp[3])
    if(rightwickets >= leftwickets):
   	dict1['m5'] = 'r'
    else:
       dict1['m5'] = 'l'
    return dict1

#------------------ query 10 --------------------#

def query10_parse(bat,info,bat1,bat2,bat3,bat4,bat5):
    list1 =[]
    for k,v in bat.iteritems():
	if v > 250:
	    list1.append(k)
    list2 =[]
    for k,v in info.iteritems():
	if v < 26:
	    list2.append(k)
    
    list3 = []
    for k,v in bat1.iteritems():
	if int(v[1]) == 0 and k not in list3:
	    list3.append(k)
    for k,v in bat2.iteritems():
	if int(v[1]) == 0 and k not in list3:
	    list3.append(k)
    for k,v in bat3.iteritems():
	if int(v[1]) == 0 and k not in list3:
	    list3.append(k)
	
    for k,v in bat4.iteritems():
	if int(v[1]) == 0 and k not in list3:
	    list3.append(k)

    for k,v in bat5.iteritems():
	if int(v[1]) == 0 and k not in list3:
	    list3.append(k)

    return list1,list2,list3


#---------------------- query 11----------------------
def query11_parse(info1,info2,info3,info4,info5):
    dict1 = {} 
    dict2 = {} 
    dict3 = {} 
    dict4 = {} 
    dict5 = {} 
    temp =[]

    for key in info1.keys():
	temp.append(key)
    dict1['play1'] = temp

    temp =[]
    for key in info2.keys():
	temp.append(key)
    dict1['play2'] = temp

    temp =[]
    for key in info3.keys():
	temp.append(key)
    dict1['play3'] = temp

    temp =[]
    for key in info4.keys():
	temp.append(key)
    dict1['play4'] = temp

    temp =[]
    for key in info5.keys():
	temp.append(key)
    dict1['play5'] = temp

    return dict1


#-------------query 12-------------#
def query12_parse(info1,info2,info3,info4,info5):
	dict1={}
	for i in info1.keys():
		if info1.get(i)[-1][-1]==')':
			#print '1'
			if i not in dict1:
				dict1[i]=int(info1.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info1.get(i)[-1][-3])
				dict1[i]=s
	for i in info2.keys():
		if info2.get(i)[-1][-1]==')':
			#print '2'
			if i not in dict1:
				dict1[i]=int(info2.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info2.get(i)[-1][-3])
				dict1[i]=s
	for i in info3.keys():
		if info3.get(i)[-1][-1]==')':
			#print '3'
			if i not in dict1:
				dict1[i]=int(info3.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info3.get(i)[-1][-3])
				dict1[i]=s
	for i in info4.keys():
		if info4.get(i)[-1][-1]==')':
			#print '4'
			if i not in dict1:
				dict1[i]=int(info4.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info4.get(i)[-1][-3])
				dict1[i]=s
	for i in info5.keys():
		if info5.get(i)[-1][-1]==')':
			if i not in dict1:
				dict1[i]=int(info5.get(i)[-1][-3])
			else:
				s=dict1[i]
				s+=int(info5.get(i)[-1][-3])
				dict1[i]=s
	dict2={}
	for i in dict1.keys():
		list1=[]
		for j in dict1.keys():
			if dict1.get(i)>dict1.get(j):
				list1.append(j)
		dict2[i]=list1
	return dict2


#-----------query 13-----------#
def query13_parse(bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10):
	dict1 = {}
	keys = bat1.keys()
	for key in keys:
		arr = bat1.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat2.keys()
	for key in keys:
		arr = bat2.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1
	

	keys = bat3.keys()
	for key in keys:
		arr = bat3.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat4.keys()
	for key in keys:
		arr = bat4.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat5.keys()
	for key in keys:
		arr = bat5.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat6.keys()
	for key in keys:
		arr = bat6.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat7.keys()
	for key in keys:
		arr = bat7.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat8.keys()
	for key in keys:
		arr = bat8.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat9.keys()
	for key in keys:
		arr = bat9.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1

	keys = bat10.keys()
	for key in keys:
		arr = bat10.get(key)[0]
		arr = arr.split(' ')
		if arr[0] == 'c':
			if(arr[1] == '&'):
				arr[1] = arr[-1]
			if arr[1] not in dict1:
				dict1[arr[1]] = 1
			else :
				dict1[arr[1]] += 1
	dict2 = {}
	for key in dict1:
		lis = []
		for value in dict1:
			if(dict1[value] > dict1[key]):
				lis.append(value)
		dict2[key]=lis

	return dict2

#----------------------query14-----------------------
def query14_parse(info1,info2,info3,info4,info5):
	dict2={}
	player1 = str(info1[1][:-1]).split('(')
    	play1 = player1[0].rstrip()
	play1=play1.lstrip()
	player2 = str(info2[1][:-1]).split('(')
    	play2 = player2[0].rstrip()
	play2=play2.lstrip()
	player3 = str(info3[1][:-1]).split('(')
    	play3 = player3[0].rstrip()
	play3=play3.lstrip()
	player4 = str(info4[1][:-1]).split('(')
    	play4 = player4[0].rstrip()
	play4=play4.lstrip()
	player5 = str(info5[1][:-1]).split('(')
    	play5 = player5[0].rstrip()
	play5=play5.lstrip()
	dict2['m1'] = play1
	dict2['m2'] = play2
        dict2['m3'] = play3
        dict2['m4'] = play4
        dict2['m5'] = play5
	#print dict2
	return dict2


#-------------- query 15 --------------#
def cal_point_wbo(score):
    if score >= 0 and score <= 0.2:
	return 1
    elif score <= 0.4:
	return 2
    elif score <= 0.6:
	return 2
    elif score <= 0.8:
	return 2
    elif score <= 1.0:
	return 2
    else:
	return 3
def cal_point_eco(score):
    if score >= 0 and score <= 3.0:
	return 1
    elif score <= 4.0:
	return 2 
    elif score <= 5.0:
	return 3 
    elif score <= 6.0:
	return 4
    elif score <= 7.0:
	return 5
    elif score <= 8.0:
	return 6
    elif score <= 9.0:
	return 7
    else:
	return 8

def cal_point_run(score):
    if score >= 0 and score< 10:
	return 10
    elif score >= 10 and score < 20:
	return 9
    elif score >= 20 and score < 30:
	return 8
    elif score >= 30 and score < 40:
	return 7
    elif score >= 40 and score < 50:
	return 6
    elif score >= 50 and score < 60:
	return 5
    elif score >= 60 and score < 70:
	return 4
    elif score >= 70 and score < 80:
	return 3
    elif score >= 80 and score < 90:
	return 2
    elif score >= 90 and score < 100:
	return 1
    else:
	return 0

def query15_parse(inn1,inn2,inn3,inn4,inn5,inn6,inn7,inn8,inn9,inn10):
    
    dict1 = {}
    for k,v in inn1.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict1[k] = points
    for k,v in inn3.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict1[k] = points
    for k,v in inn5.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict1[k] = points
    for k,v in inn7.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict1[k] = points
    for k,v in inn9.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict1[k] = points

	
    dict2 = {}
    for k,v in inn2.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict2[k] = points
    for k,v in inn4.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict2[k] = points
    for k,v in inn6.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict2[k] = points
    for k,v in inn8.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict2[k] = points
    for k,v in inn10.iteritems():
	points = 0
	points += cal_point_wbo(float(float(v[3]) / float(v[0])))
	points += int(v[1])
	points += cal_point_eco(float(v[4]))
	points += cal_point_run(int(v[2]))
	dict2[k] = points

	list1 = []
	list2 = []
	for i in dict1:
	    if i in dict2:
		if dict1[i] >= dict2[i]:
		    list1.append(i)
		else:
		    list2.append(i)

	return list1,list2
	
#-----------query 16----------#
def score(dic,dict1):
	keys = dic.keys()

	for key in keys:
		score = 0
		lis = dic.get(key)
		score = score + 4*float(lis[4])+6*float(lis[5])+5*float(lis[6])
		if key not in dict1:
			dict1[key] = score
		else:
			dict1[key] += score
def sc(dic,dict2):
	keys = dic.keys()

	for key in keys:
		score = 0
		lis = dic.get(key) 
		score = score + float(float(lis[3])/float(lis[0]))*100 - float(lis[4])

		if key not in dict2:
			dict2[key]=score
		else:
			dict2[key] += score

def query16_parse(bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10):
	dict1 = {}
	
	score(bat1,dict1)
	score(bat2,dict1)
	score(bat3,dict1)
	score(bat4,dict1)
	score(bat5,dict1)
	score(bat6,dict1)
	score(bat7,dict1)
	score(bat8,dict1)
	score(bat9,dict1)
	score(bat10,dict1)

	arr = []
	keys = dict1.keys()

	for key in keys:
		if int(dict1[key]) > 100:
			arr.append(key)
	return arr

#---------------- query 17 -------------- #
def query17_parse(bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10):
	dict1 = {}
	
	score1(bowl1,dict1)
	score1(bowl2,dict1)
	score1(bowl3,dict1)
	score1(bowl4,dict1)
	score1(bowl5,dict1)
	score1(bowl6,dict1)
	score1(bowl7,dict1)
	score1(bowl8,dict1)
	score1(bowl9,dict1)
	score1(bowl10,dict1)	
	
	arr = []
	keys = dict1.keys()
	dict2={}
	for i in dict1.keys():
		list1=[]
		for j in dict2.keys():
			if dict1[i]<dict2[j]:
				list1.append(j)
		dict2[i]=list1
	#print dict2
	return dict2
	

def score1(dic,dict1):
	score = 0
	keys = dic.keys()

	for key in keys:
		lis = dic.get(key)
		score = score + 10*float(lis[1])- 0.5*float(lis[2])+20*float(lis[3]) - float(lis[4]) + 10*float(lis[3])/float(lis[0])
		if key not in dict1:
			dict1[key] = score
		else:
			dict1[key] += score



#---------------- query 18 --------------------#
def cal_point_rbo(score):
    if score >= 0 and score <= 50:
	return 1
    elif score <= 100:
	return 2
    elif score <= 150:
	return 2
    elif score <= 200:
	return 2
    else:
	return 3
def cal_point_six(score):
    if score >=0 and score < 20:
	return 1
    elif score >= 20 and score < 25:
	return 2
    elif score >=25 and score < 32:
	return 3
    elif score >=32 and score < 40:
	return 4
    elif score >=40 and score < 60:
	return 5
    else:
	return 6


def query18_parse(bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10):

    dict1 = {}
    for k,v in bat1.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict1:
		dict1[k] = points
        elif k in dict1:
		p = (points + dict1[k])/2
		dict1[k] = p

    for k,v in bat2.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict1:
		dict1[k] = points
        elif k in dict1:
		p = (points + dict1[k])/2
		dict1[k] = p

    for k,v in bat3.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict1:
		dict1[k] = points
        elif k in dict1:
		p = (points + dict1[k])/2
		dict1[k] = p
    
    for k,v in bat4.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict1:
		dict1[k] = points
        elif k in dict1:
		p = (points + dict1[k])/2
		dict1[k] = p
    
    for k,v in bat5.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict1:
		dict1[k] = points
        elif k in dict1:
		p = (points + dict1[k])/2
		dict1[k] = p
    dict2 = {}
    for k,v in bat6.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict2:
		dict2[k] = points
        elif k in dict2:
		p = (points + dict2[k])/2
		dict2[k] = p
    for k,v in bat7.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict2:
		dict2[k] = points
        elif k in dict2:
		p = (points + dict2[k])/2
		dict2[k] = p
    for k,v in bat8.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict2:
		dict2[k] = points
        elif k in dict2:
		p = (points + dict2[k])/2
		dict2[k] = p
    for k,v in bat9.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict2:
		dict2[k] = points
        elif k in dict2:
		p = (points + dict2[k])/2
		dict2[k] = p
    for k,v in bat10.iteritems():
	points = 0
	points += cal_point_rbo(float(v[6]))
	points += cal_point_six((int(v[5])*6) + (int(v[4])*4))
	if int(v[1])==0:
	    points -= 5
	if k not in dict2:
		dict2[k] = points
        elif k in dict2:
		p = (points + dict2[k])/2
		dict2[k] = p
    dict3 = {}
    for k,v in dict2.iteritems():
	count = 0
	for l,u in dict1.iteritems():
	    if v > u :
		count += 1
		dict3[k] = count
    co=0
    list4=[]
    for k,v in dict3.iteritems():
	co+=1
	if v>=4:
		list4.append(k)

		
    return list4,co

#---------------------query19--------------------	
def query19_parse(info1,info2,info3,info4,info5):
	winner1 = str(info1[0][:-1]).split()
    	play1 = str(info1[4][:-1])
    	#play1 = player1[1].split(',')[0]
    	win1 = winner1[0]
    	if(win1 == 'New'):
		win1 = 'New Zealand'
    	elif(win1 == 'Match'):
		win1 = play1
    
    	winner2 = str(info2[0][:-1]).split()
    	play2 = str(info1[4][:-1])
    	#play2 = player2[1].split(',')[0]
    	win2 = winner2[0]
    	if(win2 == 'New'):
		win2 = 'New Zealand'
    	elif(win2 == 'Match'):
		win2 = play2

    	winner3 = str(info3[0][:-1]).split()
    	play3 = str(info3[4][:-1])
    	#play3 = player3[1].split(',')[0]
    	win3 = winner3[0]
    	if(win3 == 'New'):
		win3 = 'New Zealand'
    	elif(win3 == 'Match'):
		win3 = play3
    	winner4 = str(info4[0][:-1]).split()
    	play4 = str(info4[4][:-1])
    	#play4 = player4[1].split(',')[0]
    	win4 = winner4[0]
    	if(win4 == 'New'):
		win4 = 'New Zealand'
    	elif(win4 == 'Match'):
		win4 = play4
    	winner5 = str(info5[0][:-1]).split()
    	play5 = str(info5[4][:-1])
    	#play5 = player5[1].split(',')[0]
    	win5 = winner5[0]
    	if(win5 == 'New'):
		win5 = 'New Zealand'
    	elif(win5 == 'Match'):
		win5 = play5
    	dict1 = {}
    	dict1['m1'] = win1
    	dict1['m2'] = win2
    	dict1['m3'] = win3
    	dict1['m4'] = win4
    	dict1['m5'] = win5

    	dict2 = {}
    	dict2['m1'] = play1
    	dict2['m2'] = play2
    	dict2['m3'] = play3
    	dict2['m4'] = play4
    	dict2['m5'] = play5
	return dict1,dict2



#------------query 20---------------#
def query20_parse(bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10,bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10):
	bats = []
	bowls = []
	bats.append(bat1)
	bats.append(bat2)
	bats.append(bat3)
	bats.append(bat4)
	bats.append(bat5)
	bats.append(bat6)
	bats.append(bat7)
	bats.append(bat8)
	bats.append(bat9)
	bats.append(bat10)
	bowls.append(bowl1)
	bowls.append(bowl2)
	bowls.append(bowl3)
	bowls.append(bowl4)
	bowls.append(bowl5)
	bowls.append(bowl6)
	bowls.append(bowl7)
	bowls.append(bowl8)
	bowls.append(bowl9)
	bowls.append(bowl10)

	dict1_list = []
	dict2_list = []

	for i in bats:
		dict1 = {}
		score(i,dict1)
		dict1_list.append(dict1)

	for i in bowls:
		dict2 = {}
		sc(i,dict2)
		dict2_list.append(dict2)

	dict3 = {}
	c = 1
	for i in range(len(dict1_list)):
		lis = []
		if i%2 == 0:
			first_inning =0
			d1 = dict1_list[i]
			d2 = dict2_list[i]
			for j in d1:
				first_inning  = first_inning + float(d1[j])
			for j in d2:
				first_inning  = first_inning + float(d2[j])
		if i%2 == 1:
			d1 = dict1_list[i]
			d2 = dict2_list[i]
			second_inning = 0
			for j in d1:
				second_inning = second_inning + float(d1[j])
			for j in d2:
				second_inning = second_inning + float(d2[j])
		if i%2 == 1:
			lis.append(first_inning)
			lis.append(second_inning)
			st = 'm'+str(c)
			dict3[st] = lis
			c = c+1
	return dict3




