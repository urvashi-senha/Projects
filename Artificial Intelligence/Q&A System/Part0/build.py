from BeautifulSoup import BeautifulSoup
import urllib as u
import os

url1 = "http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html"
url2 = "http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html"
url3 = "http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html"
url4 = "http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html"
url5 = "http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html"

filename11 = "odi1_inn1_bat.txt"
filename12= "odi1_inn1_bowl.txt"
filename13 = "odi1_inn2_bat.txt"
filename14 = "odi1_inn2_bowl.txt"

filename21 = "odi2_inn1_bat.txt"
filename22= "odi2_inn1_bowl.txt"
filename23 = "odi2_inn2_bat.txt"
filename24 = "odi2_inn2_bowl.txt"

filename31 = "odi3_inn1_bat.txt"
filename32 = "odi3_inn1_bowl.txt"
filename33 = "odi3_inn2_bat.txt"
filename34 = "odi3_inn2_bowl.txt"

filename41 = "odi4_inn1_bat.txt"
filename42 = "odi4_inn1_bowl.txt"
filename43 = "odi4_inn2_bat.txt"
filename44 = "odi4_inn2_bowl.txt"

filename51 = "odi5_inn1_bat.txt"
filename52 = "odi5_inn1_bowl.txt"
filename53 = "odi5_inn2_bat.txt"
filename54 = "odi5_inn2_bowl.txt"
table1 = "inningsBat1"
table2 = "inningsBowl1"
table3 = "inningsBat2"
table4 = "inningsBowl2"


def get_html_page(url,filename,tableid,flag,winner_flag):
    	f = u.urlopen(url)
	html = f.read()

	soup = BeautifulSoup(html)

	toss = ''

	if winner_flag == 0:
		winner = soup.find('p', attrs={'class':'statusText'})
		w = str(winner)
		win = w.split('>')
#		print win[1]
		winner = win[1].split('<')
#		print winner[0]
		v = winner[0]
		fp2 = open("details.txt","a")
		fp2.write(v)
		fp2.write("\n")
		fp2.close()
	
		table1 = soup.find('table', attrs={'class' : 'notesTable'})
		rows = table1.findAll('tr')
#		print rows
		for tr in range(0,len(rows)-1):
#		    print '****'
			cols = rows[tr].findAll('td')
#		        print cols
			for td in cols:
			        list1 = str(td).split('<')
#				print list1
				for li in range(len(list1)) :
					if(str(list1[li]).find('Player of the match')!=-1):
# 						print list1[3]
#						print "found"
						b = str(list1[li+1]).split('>')
						c = b[1].replace("\n","")
#						print c				
						fp2 = open("details.txt","a")
						fp2.write(c)
						fp2.write("\n")
						fp2.close()
					if(str(list1[li]).find('Toss')!=-1):
# 						print list1[3]
#						print "found"
						b = str(list1[li+1]).split()
						toss = b[1][:-1]			
					 



		

	table = soup.find('table', id = tableid)

	rows = table.findAll('tr')

	if winner_flag == 0:
		inningdetails = rows[1].findAll('td')
#		print inningdetails
		a1 = str(inningdetails[1]).split('<')
		if(len(a1) > 1):
			a2 = str(a1[1]).split('>')
			c = a2[1]
			c= c.lstrip()
			c=c.rstrip()
			fp2 = open("details.txt","a")
			fp2.write(c)
			fp2.write("\n")
#			print c,
			if str(c) == "India innings":
#				print 'yes'
				fp2.write("New Zealand innings")
			else:
#				print 'no'
				fp2.write("India innings")
		        fp2.write("\n")
			fp2.write(toss)
		        fp2.write("\n")
			fp2.close()


	for tr in range(2,len(rows)-flag,2):
#	    	print '**********'
		data = []
		cols = rows[tr].findAll('td')
		for td in range(1,len(cols),1):
#				print '&&&&&'
#				print 'td:',
#				print td
				a = str(cols[td])
				a = a.split('>')
				if td == 1:
				    b = str(a[2])
				else:
				    b = str(a[1])

				b = b.split('<')
				c = str(b[0])
				c = c.rstrip()
				c = c.lstrip()
				c = c.replace("&amp;","&")
				c = c.replace("&dagger;","")
				if td != 1 and c != '':
				    	a = (",",c)
					s = ''
					s = s.join(a)
				else:
				    s = str(c)
#				print s
				fp = open(filename,"a")
				fp.write(str(s))
				fp.close()
#				print '&&&&&'
		fp = open(filename,"a")
		fp.write("\n")
		fp.close()
#		print '**********'
#		print ' '

def main():

#    	os.mkdir("201225020_assignment2")
#	os.chdir("./201225020_assignment2/")
    	os.mkdir("dataset")

	os.system("cp -r player_profile ./dataset")
	
	os.chdir("./dataset/")
	os.mkdir("match1")
	os.chdir("./match1/")
    	
	get_html_page(url1,filename11,table1,3,0)
	get_html_page(url1,filename12,table2,0,1)
	get_html_page(url1,filename13,table3,3,1)
	get_html_page(url1,filename14,table4,0,1)
    	
	os.chdir("../")
	os.mkdir("match2")
	os.chdir("./match2/")

	get_html_page(url2,filename21,table1,3,0)
	get_html_page(url2,filename22,table2,0,1)
	get_html_page(url2,filename23,table3,3,1)
	get_html_page(url2,filename24,table4,0,1)
	os.chdir("../")
	os.mkdir("match3")
	os.chdir("./match3/")

	get_html_page(url3,filename31,table1,3,0)
	get_html_page(url3,filename32,table2,0,1)
	get_html_page(url3,filename33,table3,3,1)
	get_html_page(url3,filename34,table4,0,1)

	os.chdir("../")
	os.mkdir("./match4")
	os.chdir("./match4/")
	get_html_page(url4,filename41,table1,3,0)
	get_html_page(url4,filename42,table2,0,1)
	get_html_page(url4,filename43,table3,3,1)
	get_html_page(url4,filename44,table4,0,1)

	os.chdir("../")
	os.mkdir("./match5")
	os.chdir("./match5/")
	get_html_page(url5,filename51,table1,3,0)
	get_html_page(url5,filename52,table2,0,1)
	get_html_page(url5,filename53,table3,3,1)
	get_html_page(url5,filename54,table4,0,1)
	os.chdir("../")
	os.chdir("../")

#	print os.getcwd()

if __name__ == "__main__":
    	main()
