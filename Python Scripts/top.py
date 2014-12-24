#!/usr/bin/python
import sys
import re
import glob
import heapq


#  Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
#  This script is used get meaning full words from 4.4 gb dataset based on frequency using min heap and then extract tweets having those keywords and dump them into respective files.


def top():
	if len(sys.argv)<1:
		print "Usage: python top.py <input-folder-path>"
		exit()
	results = sys.argv[1]

	path = results+"/*"  
	files=glob.glob(path)  

	h=[]
	K=20000
	counter=0


	topic_words=['fuck','facebook','twitter','android','iphone','pizza','internet','pink','internet','pink','jesus','sunday','safari','saber','snapchat','chelsea','friday','ipad','allah','justinbieber','arianagrande','madrid','youtube','instagram','porn','wine','argentina','bayern','google','indonesia','chocolate','venezuela','liverpool','disney','apple','london','japan','america','rihanna','obama','vilanova','whatsapp','hindi','brasil','coffee','barcelona','ronaldo','itunes','mayweather','quran','arsenal','mourinho','tumblr','skype','ukraine','manchester','torres','modi','starbucks','netflix','messi','microsoft','nasa','bible','vodka','boobs']
	for items in files:
		print items

		with open(items) as f:
			for line in f:
				ls=line.split("\t")

				if(len(str(ls[0]))>3 and (str(ls[1]) in topic_words)): #and (str(ls[0]) not in remove_words) and  (str(ls[0]) not in unsure_words)):
					if(counter<=K):
						heapq.heappush(h, (int(ls[1]),str(ls[0])))

					else:
						tupple=heapq.heappop(h)

						if(int(ls[1])<tupple[0]):
							heapq.heappush(h,tupple)
						else:
							heapq.heappush(h, (int(ls[1]),str(ls[0])))

					counter+=1
						
				#print ls[0]
				#print int(ls[1])
	tweet_seggregate(topic_words)


def tweet_seggregate(topic_words):
	pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
	#print sys.argv[1]
	counter=0
	with open(sys.argv[2]) as f:
			for line in f:
				counter+=1
				if (counter%100000) ==0:
					print "Lines read :"+ str(counter)
				line_words=pattern.findall(line)
				for topics in topic_words:
					if topics in line_words:
						f = open("topic_tweets/"+topics+".txt", "a+")
						#u' '.join("\t".join(line.split("\n"))).encode('utf-8').strip()
						f.write(str("\t".join(line.split("\n"))+"\n"))
						f.close()


if __name__ == "__main__":
	top()