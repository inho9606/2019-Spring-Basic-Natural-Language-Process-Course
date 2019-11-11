import nltk, sys
from nltk import RegexpTokenizer
from nltk import collections
from nltk import sent_tokenize
def concordance(input, mode, keyword, number):
	sys.stdout = open('./01_out/' + input.split('_')[0] + '_conc_' + keyword + '_' + mode + '.txt', 'w')
	f = open('./00_data/' + input, encoding=mode)
	token = RegexpTokenizer("\s+", gaps=True).tokenize(f.read())
	f.close()
	text = nltk.Text(token)
	text.concordance(keyword, number*2+len(keyword), lines= sys.maxsize)

def contexts(input, mode, keyword):
	sys.stdout = open('./01_out/' + input.split('_')[0] + '_cont_' + keyword + '_' + mode + '.txt', 'w')
	f = open('./00_data/' + input, encoding=mode)
	token = sent_tokenize(f.read())
	f.close()
	data = [i.split(' ') for i in token]
	list = []
	for i in data:
		for j in range(1, len(i)-1):
			if i[j].lower() == keyword.lower():
				list.append(i[j-1]+'_'+i[j+1])
	print(collections.Counter(list))

# main
concordance('data01_utf8.txt', 'utf8', 'the', 15)
concordance('data02_cp949.txt', 'cp949', 'the', 15)
contexts('data01_utf8.txt', 'utf8', 'the')
contexts('data02_cp949.txt', 'cp949', 'the')
