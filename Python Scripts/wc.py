#!/usr/bin/python
import sys
import re


#  Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
#  This script MAPPER for Hadoop . This is used to put one with each word of sentence. It also contains words to be omitted
     
def main(argv):
	words_remove=['with','its','take','she','day','were','do','call','it','be','part','now','his','all','we','on','did','cd','from','does','the','them','said','of','two','as','time','case','or','here','when','very','each','go','send','same','both','list','info','item','he','off','pm','is','more','add','been','must','see','who','end','area','type','own','for','have','down','had','usa','link','non','jan','make','into','me','file','that','mail','such','are','my','no','than','find','get','her','form','your','can','show','user','line','back','name','rate','new','ebay','any','has','made','open','one','an','and','use','know','just','text','re','us','then','you','to','may','they','why','long','how','want','only','map','per','so','uk','way','used','days','will','dvd','not','up','some','code','if','in','this','was','care','even','what','much','but','big','law','set','real','save','many','sign','size','also','our','date','at','john','out','main','need','him','over','by','car','year','am','old','next']
	line = sys.stdin.readline()
	pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
	try:
		while line:
			for word in  pattern.findall(line):
				if word not in words_remove:
					print  "LongValueSum:" + word.lower() + "\t" + "1"
			line =  sys.stdin.readline()
	except "end of file":
		return None

if __name__ == "__main__":
	main(sys.argv)
