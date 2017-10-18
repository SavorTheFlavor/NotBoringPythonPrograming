import re

def wordcount(text_file):
	dic = {}
	with open(text_file) as tf:
		while(True):
			line = tf.readline()
			if(not line): 
				break
			if(line.strip() == ''):
				continue
			words = re.split(r'[\s=,?.!:""“”]+',line)
			for word in words:
				count = 0
				if(word == ''):
					continue
				if(word in dic):
					count = dic.get(word) + 1
				dic.update({word:count})
	return dic

if __name__ == '__main__':
	text_file = 'Jane Eyre.txt'
	words = wordcount(text_file)
	res=sorted(words.items(),key=lambda word:word[1],reverse=True)
	print(res[:10])