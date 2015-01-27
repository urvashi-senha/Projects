import urllib
import os

l = ['Thumb','Index','Middle','Ring','Little']


count = 1
for i in range(16): 
    for j in l:
	url = 'http://www.unilorin.edu.ng/step-b/biometrics/Female/Prints/' +  'LFinger/' + str(j) + '/f' + str(i) + '.bmp'
	image=urllib.URLopener()
      	name = str(count) + '.bmp'
	count+=1
    	image.retrieve(url,name)
    for k in l:
	url = 'http://www.unilorin.edu.ng/step-b/biometrics/Female/Prints/' +  'RFinger/' + str(j) + '/f' + str(i) + '.bmp'
	name = str(count) + '.bmp'
	count+=1
	image=urllib.URLopener()
    	image.retrieve(url,name)
