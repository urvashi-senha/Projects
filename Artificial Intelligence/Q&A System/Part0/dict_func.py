# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
    f = open(fname, 'r')
    for line in f:
		    temp = line[:-1]
		    temp = temp.split(',')
		    a = temp[0]
		    b = temp[1:]
		    if a not in dictionary:
			dictionary[a] = b

def parse_detail(dictionary,fname):
    f = open(fname, 'r')
    count = 0
    for line in f:
	dictionary[count] = line[0:-1]
	count = count + 1

def player_details(dictionary,fname):
    f = open(fname, 'r')
    count = 0
    for line in f:
	temp = line[-1]
	temp = line.split('\t')
	age = str(temp[3]).split()
	a = int(age[0])
	if temp[0] not in dictionary:
		dictionary[temp[0]] = a
	count = count + 1

def run_dict(dictionary, fname):
    f = open(fname, 'r')
    for line in f:
		    temp = line[:-1]
		    temp = temp.split(',')
		    a = temp[0]
		    b = temp[1:]
		    if a not in dictionary:
			dictionary[a] = int(b[1])
		    elif a in dictionary:
			value = dictionary[a] + int(b[1])
			dictionary[a] = value

def get_openers(dictionary,fname):
    f = open(fname,'r')
    count = 1
    for line in f :
	if count < 3:
	    temp = line[:-1]
	    temp = temp.split(',')
	    a = temp[0]
	    b= temp[1:]
	    if a not in dictionary:
		dictionary[a] = b
	else:
	    break
	count += 1    

def get_middle(dictionary,fname):
    f = open(fname,'r')
    count = 1
    for line in f :
	if count >= 5 and count <=7:
	    temp = line[:-1]
	    temp = temp.split(',')
	    a = temp[0]
	    b= temp[1:]
	    if a not in dictionary:
		dictionary[a] = b
	elif count > 9:
	    break
	count += 1    

def player_details2(dictionary,fname):
    f = open(fname, 'r')
   
    for line in f:
	temp = line[-1]
	temp = line.split('\t')
	a = str(temp[-1])
	if(a.find('Right') != -1): 
		if temp[0] not in dictionary:
			dictionary[temp[0]] = 'Right'
	else:
		if temp[0] not in dictionary:
			dictionary[temp[0]] = 'Left'

