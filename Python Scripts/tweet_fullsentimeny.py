import sys
import re
import glob
from textblob import TextBlob
from collections import defaultdict
import operator
import glob
import random
import datetime

#  Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
#  This script is used to get sentiment of full tweet using the dictionary of positive and negative words each having score.
# to run : time python tweet_fullsentimeny.py topic_tweets

p=dict(defaultdict(float))
n=dict(defaultdict(float))


def full():
	with open("/Users/umang/Documents/assi3_cloud/COMBINE_POSITIVE.txt") as f:
		for line in f:
			#print line
			if(line !=" "):
				l=line.strip("\n").split(" ")
				#print len(l)
				#print l
				p[l[0]]=float(l[1])

	f.close()			
	with open("/Users/umang/Documents/assi3_cloud/COMBINE_NEGATIVE.txt") as f:
		for line in f: 
			if(line !=" "):
				l=line.strip("\n").split(" ")
				#print l
				n[l[0]]=float(l[1])		

	#print n
	#print p		

	folder_path=sys.argv[1]+"/"
	files=["android","twitter","justinbieber","ipad","internet","pink","snapchat","youtube","chocolate","facebook","coffee","allah","disney","apple","madrid","christmas"]

	counter=0
	for file1 in files:
		with open(folder_path+file1+".txt") as f:



			score_file= open("NO_NEUTRAL_SCORE_"+file1+".txt", "w+")

			for line in f:
				#print line

				counter+=1
				print file1+"->"+str(counter)


				wl=line.replace("@","").replace("!","").replace("#","").replace("'","").replace(")","").replace(":","").replace("?","").lower().split()

				score=0
				occured=0
				for words in wl:
					if words in p:
						score+=p[words]
						occured=1
					elif words in n:
						score+=n[words]
						occured=1
				
				if occured==0:
					w= TextBlob(line.decode('utf-8'))
					#print line
					pol=w.sentiment.polarity
					if pol==0:
						#print 0.2
						randtemp=random.randint(1,2)
						if randtemp==1:
							print "Neglected"
							#---->score_file.write(str(0.2)+"\n")
						else:
							#----->score_file.write(str(-0.2)+"\n")
							print "Neglected"
								
				else:
					#print score
					score_file.write(str(score)+"\n")	
				#print "--------------------------------"			

			score_file.close()
			
		f.close()
	tsvdata()

def tsvdata():
	files=["android","twitter","justinbieber","ipad","internet","pink","snapchat","youtube","chocolate","facebook","coffee","allah","disney","apple","madrid","christmas"]

	for file1 in files:
		lines= open("NO_NEUTRAL_SCORE_"+file1+".txt").readlines()

		wf=open("SCORE_"+file1+".txt","w+")
		wf.write("label"+"\t"+"value"+"\n")

		stime=datetime.datetime(2014,4,21,20,00)

		nbard=29
		eachtweets=len(lines)/nbard

		for i in range(nbard):
			pos=0
			neg=0
			templist=lines[i*eachtweets:((i+1)*eachtweets)]



			for val in templist:
				valstrip=float(val.rstrip())
				if valstrip >0:
					#pos+=valstrip
					pos+=1
				elif valstrip <0:
					#neg+=valstrip	
					neg-=1

			label=stime.strftime("%m/%d %H:%M")
			wf.write(label+"\t"+str(pos/float(pos-neg))+"\n")
			wf.write(label+"\t"+str(neg/float(pos-neg))+"\n")

			stime=stime+datetime.timedelta(hours=8)		

		wf.close()
			
if __name__ == "__main__":
	full()
	#tsvdata()