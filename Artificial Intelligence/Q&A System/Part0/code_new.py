import nltk
import sys
import dict_func
import new
import var_pair
import make_model
#------------- Variables ------------------#

file11 = './dataset/match1/odi1_inn1_bat.txt'
file12 = './dataset/match1/odi1_inn1_bowl.txt'
file13 = './dataset/match1/odi1_inn2_bat.txt'
file14 = './dataset/match1/odi1_inn2_bowl.txt'
file15 = './dataset/match1/details.txt'

file21 = './dataset/match2/odi2_inn1_bat.txt'
file22 = './dataset/match2/odi2_inn1_bowl.txt'
file23 = './dataset/match2/odi2_inn2_bat.txt'
file24 = './dataset/match2/odi2_inn2_bowl.txt'
file25 = './dataset/match2/details.txt'

file31 = './dataset/match3/odi3_inn1_bat.txt'
file32 = './dataset/match3/odi3_inn1_bowl.txt'
file33 = './dataset/match3/odi3_inn2_bat.txt'
file34 = './dataset/match3/odi3_inn2_bowl.txt'
file35 = './dataset/match3/details.txt'

file41 = './dataset/match4/odi4_inn1_bat.txt'
file42 = './dataset/match4/odi4_inn1_bowl.txt'
file43 = './dataset/match4/odi4_inn2_bat.txt'
file44 = './dataset/match4/odi4_inn2_bowl.txt'
file45 = './dataset/match4/details.txt'

file51 = './dataset/match5/odi5_inn1_bat.txt'
file52 = './dataset/match5/odi5_inn1_bowl.txt'
file53 = './dataset/match5/odi5_inn2_bat.txt'
file54 = './dataset/match5/odi5_inn2_bowl.txt'
file55 = './dataset/match5/details.txt'

file2 = './dataset/player_profile/indian_players_profile.txt'
file3 = './dataset/player_profile/nz_players_profile.txt'

#---------------------------------------------#

def main():

  print "#------------ query 1 --------------#\n"

  info1 = {}
  info2 = {}
  info3 = {}
  info4 = {}
  info5 = {}
  dict_func.parse_detail(info1,file15);
  dict_func.parse_detail(info2,file25);
  dict_func.parse_detail(info3,file35);
  dict_func.parse_detail(info4,file45);
  dict_func.parse_detail(info5,file55);
    
  q1 = {}
  q2 = {}
  name_to_var1 ={}
  v1 = ''
  query1 =''
  parse1 =''
  q1,q2 = new.query1_parse(info1,info2,info3,info4,info5);
  v1,query1,name_to_var1,parse1 = var_pair.var_pair1(q1,q2)
  make_model.make(v1,query1,parse1,name_to_var1)

  print   "#------------ query 2 -------------------#\n"
  bats1 = {}
  bats2 = {}
  bats3 = {}
  bats4 = {}
  bats5 = {}
  bats6 = {}
  bats7 = {}
  bats8 = {}
  bats9 = {}
  bats10 = {}
    
  info1 = {}
  info2 = {}
  info3 = {}
  info4 = {}
  info5 = {}
  q1 = {}
  q2 = {}

  dict_func.add_to_dict(bats1,file11);
  dict_func.add_to_dict(bats2,file13);
  dict_func.add_to_dict(bats3,file21);
  dict_func.add_to_dict(bats4,file23);
  dict_func.add_to_dict(bats5,file31);
  dict_func.add_to_dict(bats6,file33);
  dict_func.add_to_dict(bats7,file41);
  dict_func.add_to_dict(bats8,file43);
  dict_func.add_to_dict(bats9,file51);
  dict_func.add_to_dict(bats10,file53);
  dict_func.parse_detail(info1,file15);
  dict_func.parse_detail(info2,file25);
  dict_func.parse_detail(info3,file35);
  dict_func.parse_detail(info4,file45);
  dict_func.parse_detail(info5,file55);
    
  q1,q2 = new.query2_parse(info1,info2,info3,info4,info5,bats1,bats2,bats3,bats4,bats5,bats6,bats7,bats8,bats9,bats10);
  #print q1
  #print q2
  v2,query2,name_to_var2,parse2 = var_pair.var_pair2(q1,q2)
  make_model.make(v2,query2,parse2,name_to_var2)

  print "#------------ query 3 -------------------#"
  info1={}
  info2={}
  info3={}
  info4={}
  info5={}
  info6={}
  info7={}
  info8={}
  info9={}
  info10={}

    
  dict_func.add_to_dict(info1,file11);
  dict_func.add_to_dict(info2,file21);
  dict_func.add_to_dict(info3,file31);
  dict_func.add_to_dict(info4,file41);
  dict_func.add_to_dict(info5,file51);
  dict_func.add_to_dict(info6,file13);
  dict_func.add_to_dict(info7,file23);
  dict_func.add_to_dict(info8,file33);
  dict_func.add_to_dict(info9,file43);
  dict_func.add_to_dict(info10,file53);

#   print info1
    
  q1 = {}
  q2 = {}
  name_to_var3 ={}
  v3 = ''
  query3 =''
  parse3 =''
  q1,q2 = new.query3_parse(info1,info2,info3,info4,info5,info6,info7,info8,info9,info10);
  v3,query3,name_to_var3,parse3 = var_pair.var_pair3(q1,q2)
  make_model.make(v3,query3,parse3,name_to_var3)


  print "#-----------query 4 ------------------------------#\n"
    
  bat1 = {}
  bat2 = {}
  bat3 = {}
  bat4 = {}
  bat5 = {}
  q1 = {}
  q2 = {}
  dict_func.parse_detail(bat1,file11);
  dict_func.parse_detail(bat2,file21);
  dict_func.parse_detail(bat3,file31);
  dict_func.parse_detail(bat4,file41);
  dict_func.parse_detail(bat5,file51);
  q1,q2 = new.query4_parse(bat1,bat2,bat3,bat4,bat5)
  v4,query4,name_to_var4,parse4 = var_pair.var_pair4(q1,q2)
  make_model.make(v4,query4,parse4,name_to_var4)


  print "#------------- query 5 -----------------#\n"
  bowl1 = {}
  bowl2 = {}
  bowl3 = {}
  bowl4 = {}
  bowl5 = {}
  bats1 = {}
  bats2 = {}
  bats3 = {}
  bats4 = {}
  bats5 = {}
  q1 = {}
  q2 = {}

  dict_func.add_to_dict(bats1,file11)
  dict_func.add_to_dict(bats1,file13)
  dict_func.add_to_dict(bats2,file21)
  dict_func.add_to_dict(bats2,file23)
  dict_func.add_to_dict(bats3,file31)
  dict_func.add_to_dict(bats3,file32)
  dict_func.add_to_dict(bats4,file41)
  dict_func.add_to_dict(bats4,file43)
  dict_func.add_to_dict(bats5,file51)
  dict_func.add_to_dict(bats5,file53)
    
  dict_func.add_to_dict(bowl1,file12)
  dict_func.add_to_dict(bowl1,file14)
  dict_func.add_to_dict(bowl2,file22)
  dict_func.add_to_dict(bowl2,file24)
  dict_func.add_to_dict(bowl3,file32)
  dict_func.add_to_dict(bowl3,file34)
  dict_func.add_to_dict(bowl4,file42)
  dict_func.add_to_dict(bowl4,file44)
  dict_func.add_to_dict(bowl5,file52)
  dict_func.add_to_dict(bowl5,file54)

  q1,q2 = new.query5_parse(bats1,bats2,bats3,bats4,bats5,bowl1,bowl2,bowl3,bowl4,bowl5)
  v5,query5,name_to_var5,parse5 = var_pair.var_pair5(q1,q2)
  make_model.make(v5,query5,parse5,name_to_var5)

  print "#---------------query 6------#\n"
  bowl1 = {}
  bowl2 = {}
  bowl3 = {}
  bowl4 = {}
  bowl5 = {}
  bowl6 = {}
  bowl7 = {}
  bowl8 = {}
  bowl9 = {}
  bowl10 = {}
  q1={}
  q2={}
  dict_func.add_to_dict(bowl1,file12);
  dict_func.add_to_dict(bowl2,file14);
  dict_func.add_to_dict(bowl3,file22);
  dict_func.add_to_dict(bowl4,file24);
  dict_func.add_to_dict(bowl5,file32);
  dict_func.add_to_dict(bowl6,file34);
  dict_func.add_to_dict(bowl7,file42);
  dict_func.add_to_dict(bowl8,file44);
  dict_func.add_to_dict(bowl9,file52);
  dict_func.add_to_dict(bowl10,file54);
  q1,q2 = new.query6_parse(bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10);

  name_to_var6 ={}
  v6 = ''
  query6 =''
  parse6 =''
  v6,query6,name_to_var6,parse6 = var_pair.var_pair6(q1,q2)
  make_model.make(v6,query6,parse6,name_to_var6)

  print "#-----------query 7 ------------------------------#"
  bowl1 = {}
  bowl2 = {}
  bowl3 = {}
  bowl4 = {}
  bowl5 = {}
  bowl6 = {}
  bowl7 = {}
  bowl8 = {}
  bowl9 = {}
  bowl10 = {}
  q1 = {}
  q2 = {}
  dict_func.add_to_dict(bowl1,file12);
  dict_func.add_to_dict(bowl2,file14);
  dict_func.add_to_dict(bowl3,file22);
  dict_func.add_to_dict(bowl4,file24);
  dict_func.add_to_dict(bowl5,file32);
  dict_func.add_to_dict(bowl6,file34);
  dict_func.add_to_dict(bowl7,file42);
  dict_func.add_to_dict(bowl8,file44);
  dict_func.add_to_dict(bowl9,file52);
  dict_func.add_to_dict(bowl10,file54);

  q1,q2 = new.query7_parse(bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10)

  #print q1
  #print q2
    
  v7,query7,name_to_var7,parse7 = var_pair.var_pair7(q1,q2)
  #print v7
  #print query7
  #print name_to_var7
  #print parse7
  make_model.make(v7,query7,parse7,name_to_var7)


  print "#-------------- query 8 ----------------- #"

  bats1 = {}
  bats2 = {}
  bats3 = {}
  bats4 = {}
  bats5 = {}
  bats6 = {}
  bats7 = {}
  bats8 = {}
  bats9 = {}
  bats10 = {}
  info1 = {}
  info2 = {}
  info3 = {}
  info4 = {}
  info5 = {}
  q1 = {}
  q2 = {}


  dict_func.add_to_dict(bats1,file11);
  dict_func.add_to_dict(bats2,file13);
  dict_func.add_to_dict(bats3,file21);
  dict_func.add_to_dict(bats4,file23);
  dict_func.add_to_dict(bats5,file31);
  dict_func.add_to_dict(bats6,file33);
  dict_func.add_to_dict(bats7,file41);
  dict_func.add_to_dict(bats8,file43);
  dict_func.add_to_dict(bats9,file51);
  dict_func.add_to_dict(bats10,file53);
  dict_func.parse_detail(info1,file15);
  dict_func.parse_detail(info2,file25);
  dict_func.parse_detail(info3,file35);
  dict_func.parse_detail(info4,file45);
  dict_func.parse_detail(info5,file55);
  q1,q2 = new.query8_parse(info1,info2,info3,info4,info5,bats1,bats2,bats3,bats4,bats5,bats6,bats7,bats8,bats9,bats10);
  v8,query8,name_to_var8,parse8 = var_pair.var_pair8(q1,q2)
  make_model.make(v8,query8,parse8,name_to_var8)
  print "#------------ query 9 -------------#\n"

  bowl1 = {}
  bowl2 = {}
  bowl3 = {}
  bowl4 = {}
  bowl5 = {}
  info1 = {}
  q1 = {}
  dict_func.player_details2(info1,file2)
  dict_func.player_details2(info1,file3)
  #print info1
 
  dict_func.add_to_dict(bowl1,file12)
  dict_func.add_to_dict(bowl1,file14)
  dict_func.add_to_dict(bowl2,file22)
  dict_func.add_to_dict(bowl2,file24)
  dict_func.add_to_dict(bowl3,file32)
  dict_func.add_to_dict(bowl3,file34)
  dict_func.add_to_dict(bowl4,file42)
  dict_func.add_to_dict(bowl4,file44)
  dict_func.add_to_dict(bowl5,file52)
  dict_func.add_to_dict(bowl5,file54)
  q1 = new.query9_parse(info1,bowl1,bowl2,bowl3,bowl4,bowl5)
  #print q1
  v9,query9,parse9,name_to_var9 = var_pair.var_pair9(q1,)
  #print v10
  #print query10
  #print name_to_var2
  #print parse10
  make_model.make(v9,query9,parse9,name_to_var9)

  print "#-------------- query 10 ----------------------#\n"
  bats1 = {}
  bats2 = {}
  bats3 = {}
  bats4 = {}
  bats5 = {}
  
  bats = {}
  info = {}
  q1 = []
  q2 = []
  q3 = []
  dict_func.add_to_dict(bats1,file11)
  dict_func.add_to_dict(bats1,file13)
  dict_func.add_to_dict(bats2,file21)
  dict_func.add_to_dict(bats2,file23)
  dict_func.add_to_dict(bats3,file31)
  dict_func.add_to_dict(bats3,file32)
  dict_func.add_to_dict(bats4,file41)
  dict_func.add_to_dict(bats4,file43)
  dict_func.add_to_dict(bats5,file51)
  dict_func.add_to_dict(bats5,file53)
  
  dict_func.run_dict(bats,file11)
  dict_func.run_dict(bats,file13)
  dict_func.run_dict(bats,file21)
  dict_func.run_dict(bats,file23)
  dict_func.run_dict(bats,file31)
  dict_func.run_dict(bats,file33)
  dict_func.run_dict(bats,file41)
  dict_func.run_dict(bats,file43)
  dict_func.run_dict(bats,file51)
  dict_func.run_dict(bats,file53)
  dict_func.player_details(info,file2)
  dict_func.player_details(info,file3)
  #print bats
  #print info

  q1,q2,q3 = new.query10_parse(bats,info,bats1,bats2,bats3,bats4,bats5)
  #print q1
  #print q2
  #print q3
   
  v10,query10,parse10,name_to_var10 = var_pair.var_pair10(q1,q2,q3)
  #print v10
  #print query10
  #print name_to_var2
  #print parse10
  make_model.make(v10,query10,parse10,name_to_var10)
  print "#-----------------------------query 11--------------------#\n"


  info1 = {}
  info2 = {}
  info3 = {}
  info4 = {}
  info5 = {}
  dict_func.add_to_dict(info1,file11)
  dict_func.add_to_dict(info1,file12)
  dict_func.add_to_dict(info1,file13)
  dict_func.add_to_dict(info1,file14)
  dict_func.add_to_dict(info2,file21)
  dict_func.add_to_dict(info2,file22)
  dict_func.add_to_dict(info2,file23)
  dict_func.add_to_dict(info2,file24)
  dict_func.add_to_dict(info3,file31)
  dict_func.add_to_dict(info3,file32)
  dict_func.add_to_dict(info3,file33)
  dict_func.add_to_dict(info3,file34)
  dict_func.add_to_dict(info4,file41)
  dict_func.add_to_dict(info4,file42)
  dict_func.add_to_dict(info4,file43)
  dict_func.add_to_dict(info4,file44)
  dict_func.add_to_dict(info5,file51)
  dict_func.add_to_dict(info5,file52)
  dict_func.add_to_dict(info5,file53)
  dict_func.add_to_dict(info5,file54)
  q1 = {}
  
#print info1
  q1= new.query11_parse(info1,info2,info3,info4,info5)
   #  q1 = new.query11_parse(info1,info2,info3,info4,info5)
  var_pair.var_pair11(q1)


  print "#-----------query 12-------------------------#\n"
  player={}
  info1={}
  info2={}
  info3={}
  info4={}
  info5={} 
  dict_func.add_to_dict(info1,file12);
  dict_func.add_to_dict(info2,file22);
  dict_func.add_to_dict(info3,file32);
  dict_func.add_to_dict(info4,file44);
  dict_func.add_to_dict(info5,file52);
  #print info1
  q1={}
  query3 =''
  q1 = new.query12_parse(info1,info2,info3,info4,info5);
  #print q1
  var_pair.var_pair12(q1)

  print "#-----------query 13 ------------------------------#\n"
  bat1 = {}
  bat2 = {}
  bat3 = {}
  bat4 = {}
  bat5 = {}
  bat6 = {}
  bat7 = {}
  bat8 = {}
  bat9 = {}
  bat10 = {}
  q1 = {} 
  # q1 store people who took more catches than Ryder
  dict_func.add_to_dict(bat1,file11);
  dict_func.add_to_dict(bat2,file13);
  dict_func.add_to_dict(bat3,file21);
  dict_func.add_to_dict(bat4,file23);
  dict_func.add_to_dict(bat5,file31);
  dict_func.add_to_dict(bat6,file33);
  dict_func.add_to_dict(bat7,file41);
  dict_func.add_to_dict(bat9,file51);
  dict_func.add_to_dict(bat10,file53);

  q1 = new.query13_parse(bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10)

  var_pair.var_pair13(q1)


  print "#------------------query14----------------------------------------#\n"
  info1={}
  info2={}
  info3={}
  info4={}
  info5={}
  dict_func.parse_detail(info1,file15);
  dict_func.parse_detail(info2,file25);
  dict_func.parse_detail(info3,file35);
  dict_func.parse_detail(info4,file45);
  dict_func.parse_detail(info5,file55);
  
  q1 = {}
  name_to_var14 ={}
  v14 = ''
  query14 =''
  parse14 =''
  q1 = new.query14_parse(info1,info2,info3,info4,info5);
# print q1 
# print q2
  var_pair.var_pair14(q1)
# print v1 
#  print query1	

  print "#---------- query 15 --------------#\n"

  inn1 = {}
  inn2 = {}
  inn3 = {}
  inn4 = {}
  inn5 = {}
  inn6 = {}
  inn7 = {}
  inn8 = {}
  inn9 = {}
  inn10 = {}
  q1 = []
  q2 = []
  dict_func.add_to_dict(inn1,file12)
  dict_func.add_to_dict(inn2,file14)
  dict_func.add_to_dict(inn3,file22)
  dict_func.add_to_dict(inn4,file24)
  dict_func.add_to_dict(inn5,file32)
  dict_func.add_to_dict(inn6,file34)
  dict_func.add_to_dict(inn7,file42)
  dict_func.add_to_dict(inn8,file44)
  dict_func.add_to_dict(inn9,file52)
  dict_func.add_to_dict(inn10,file54)
  q1,q2 = new.query15_parse(inn1,inn2,inn3,inn4,inn5,inn6,inn7,inn8,inn9,inn10)

  #print q1
  #print q2
  var_pair.var_pair15(q1,q2)

  print "#-----------query16 ------------------------------#\n"
  bat1 = {}
  bat2 = {}
  bat3 = {}
  bat4 = {}
  bat5 = {}
  bat6 = {}
  bat7 = {}
  bat8 = {}
  bat9 = {}
  bat10 = {}
  arr = [] 
  # q1 stores hard-hitting batsman
  dict_func.add_to_dict(bat1,file11);
  dict_func.add_to_dict(bat2,file13);
  dict_func.add_to_dict(bat3,file21);
  dict_func.add_to_dict(bat4,file23);
  dict_func.add_to_dict(bat5,file31);
  dict_func.add_to_dict(bat6,file33);
  dict_func.add_to_dict(bat7,file41);
  dict_func.add_to_dict(bat8,file43);
  dict_func.add_to_dict(bat9,file51);
  dict_func.add_to_dict(bat10,file53);
  arr = new.query16_parse(bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10)

    
    
  var_pair.var_pair16(arr)

  print "#-----------query 17 ------------------------------#\n"
  bowl1 = {}
  bowl2 = {}
  bowl3 = {}
  bowl4 = {}
  bowl5 = {}
  bowl6 = {}
  bowl7 = {}
  bowl8 = {}
  bowl9 = {}
  bowl0 = {}
  arr = [] 
  # q1 stores hard-hitting batsman
  dict_func.add_to_dict(bowl1,file12);
  dict_func.add_to_dict(bowl2,file14);
  dict_func.add_to_dict(bowl3,file22);
  dict_func.add_to_dict(bowl4,file24);
  dict_func.add_to_dict(bowl5,file32);
  dict_func.add_to_dict(bowl6,file34);
  dict_func.add_to_dict(bowl7,file42);
  dict_func.add_to_dict(bowl8,file44);
  dict_func.add_to_dict(bowl9,file52);
  dict_func.add_to_dict(bowl10,file54);
  arr = new.query17_parse(bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10)
  var_pair.var_pair17(arr)


  print "#------------- query 18 -------------#\n"
    
  bats1 = {}
  bats2 = {}
  bats3 = {}
  bats4 = {}
  bats5 = {}
  bats6 = {}
  bats7 = {}
  bats8 = {}
  bats9 = {}
  bats10 = {}
  q1 = {}
  q2 = {}
  q3 = {}
  dict_func.get_openers(bats1,file11)
  dict_func.get_openers(bats1,file13)
  dict_func.get_openers(bats2,file21)
  dict_func.get_openers(bats2,file23)
  dict_func.get_openers(bats3,file31)
  dict_func.get_openers(bats3,file33)
  dict_func.get_openers(bats4,file41)
  dict_func.get_openers(bats4,file43)
  dict_func.get_openers(bats5,file51)
  dict_func.get_openers(bats5,file53)
  dict_func.get_middle(bats6,file11)
  dict_func.get_middle(bats6,file13)
  dict_func.get_middle(bats7,file21)
  dict_func.get_middle(bats7,file23)
  dict_func.get_middle(bats8,file31)
  dict_func.get_middle(bats8,file33)
  dict_func.get_middle(bats9,file41)
  dict_func.get_middle(bats9,file43)
  dict_func.get_middle(bats10,file51)
  dict_func.get_middle(bats10,file53)
  
  cou=0
  q3,cou = new.query18_parse(bats1,bats2,bats3,bats4,bats5,bats6,bats7,bats8,bats9,bats10)

  #print q3
  var_pair.var_pair18(q3,cou)
  print "#---------------query 19------------------------------#"
  info1={}
  info2={}
  info3={}
  info4={}
  info5={}
  dict_func.parse_detail(info1,file15);
  dict_func.parse_detail(info2,file25);
  dict_func.parse_detail(info3,file35);
  dict_func.parse_detail(info4,file45);
  dict_func.parse_detail(info5,file55);
  
  q1 = {}
  q2 = {}
  name_to_var19 ={}
  v19 = ''
  query19 =''
  parse19 =''
  q1,q2 = new.query19_parse(info1,info2,info3,info4,info5);
#  print q1 
#  print q2
  var_pair.var_pair19(q1,q2)
# print v1 
#  print query1
  #make_model.make(v19,query19,parse19,name_to_var19)

  print "#-----------query 20 ------------------------------#\n"
  bat1 = {}
  bat2 = {}
  bat3 = {}
  bat4 = {}
  bat5 = {}
  bat6 = {}
  bat7 = {}
  bat8 = {}
  bat9 = {}
  bat10 = {}
  bowl1 = {}
  bowl2 = {}
  bowl3 = {}
  bowl4 = {}
  bowl5 = {}
  bowl6 = {}
  bowl7 = {}
  bowl8 = {}
  bowl9 = {}
  bowl10 = {}
  dict1 = {}
  info1 = {}
  info2 = {}
  info3 = {}
  info4 = {}
  info5 = {}
  # q1 stores hard-hitting batsman
  dict_func.add_to_dict(bat1,file11);
  dict_func.add_to_dict(bat2,file13);
  dict_func.add_to_dict(bat3,file21);
  dict_func.add_to_dict(bat4,file23);
  dict_func.add_to_dict(bat5,file31);
  dict_func.add_to_dict(bat6,file33);
  dict_func.add_to_dict(bat7,file41);
  dict_func.add_to_dict(bat8,file43);
  dict_func.add_to_dict(bat9,file51);
  dict_func.add_to_dict(bat10,file53);
  dict_func.add_to_dict(bowl1,file12);
  dict_func.add_to_dict(bowl2,file14);
  dict_func.add_to_dict(bowl3,file22);
  dict_func.add_to_dict(bowl4,file24);
  dict_func.add_to_dict(bowl5,file32);
  dict_func.add_to_dict(bowl6,file34);
  dict_func.add_to_dict(bowl7,file42);
  dict_func.add_to_dict(bowl8,file44);
  dict_func.add_to_dict(bowl9,file52);
  dict_func.add_to_dict(bowl10,file54);
  dict_func.parse_detail(info1,file15);
  dict_func.parse_detail(info2,file25);
  dict_func.parse_detail(info3,file35);
  dict_func.parse_detail(info4,file45);
  dict_func.parse_detail(info5,file55);

  dict1 = new.query20_parse(bat1,bat2,bat3,bat4,bat5,bat6,bat7,bat8,bat9,bat10,bowl1,bowl2,bowl3,bowl4,bowl5,bowl6,bowl7,bowl8,bowl9,bowl10)
  #print dict1

  q1 = {}
  q2 = {}
  q1,q2 = new.query2_parse(info1,info2,info3,info4,info5,bats1,bats2,bats3,bats4,bats5,bats6,bats7,bats8,bats9,bats10)
  #print q1

  dict2 = {}
  for i in dict1:
  	lis = dict1.get(i)
	if(lis[0]< lis[1]):
		dict2[i] = q1[i]
	elif(lis[0] > lis[1]):
		if(q1[i] == 'New Zealand'):
			  dict2[i] = 'India'
		else:
			  dict2[i] = 'New Zealand'
  #print dict2
  var_pair.var_pair20(dict2)
    
   
if __name__ == "__main__":
    main()
