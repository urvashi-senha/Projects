from pybrain.datasets import SupervisedDataSet


def conversion_to_pybrain_dataset_format(training_data):
    ds = SupervisedDataSet(28, 39)
    count = 0
    for inp,out in training_data:
	if count <= 500 :
	  indata =  tuple(inp[:])
	  outdata = tuple(out[:])
	  ds.addSample(indata,outdata)
	  count += 1
	else:
	    break
    return ds


def conversion_to_one_hot_representation():

    # ENGLISH - 26 APLPHABETS + ' + -
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','\'','-']

    # ARPA PHONESET IS USED - 39 PHONES
    file_phones = open("cmudict.phones","r")
    phones = []
    for line in file_phones:
	i = line.split()
	phones.append(i[0])
    
    # DICTIONARY IS STORED AS LIST OF TUPLES - (WORD,PHONEMES)
    file_dict = open("cmudict.dict","r")
    training_data = []
    for line in file_dict:
	i = line.split()
	
	#removing word number
	if(len(i[0])>=4 ) and (i[0][-3]=='('):
		i[0] = i[0][:-3]

	#converting word to one-hot vector representation
	word = [ 0 for x in range(28) ]
	for x in i[0]:
	    word[alphabet.index(x)] = 1

	phonemes = [ 0 for x in range(39) ]
	for x in range(1,len(i)):
	    
	    # removing stress markers
	    if (len(i[x])>=2) and (i[x][-1] == '0' or i[x][-1] == '1' or i[x][-1] == '2'):
		    i[x] = i[x][:-1]
	    
	    #converting phones to one-hot vector representation
	    phonemes[phones.index(i[x])] = 1
	training_data.append((word,phonemes))
    return training_data


