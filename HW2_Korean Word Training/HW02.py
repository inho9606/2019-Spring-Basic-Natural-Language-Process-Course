#-*- coding: utf-8 -*-
import nltk, re
def features(w):
	form = {}
	if 'No1.' in w or '기자:' in w or '감독' in w or '기자]' in w: form['crm'] = 1
	if '제이미' in w or '박세운' in w or '퍼거슨' in w or '이석무' in w or '이종열' in w: form['per'] = 1
	if '서울' in w or '코리아' in w or '공단' in w or '삼성' in w or '현대' in w or 'LG' in w or '대학교' in w or '협회' in w or '그룹' in w or '영사관' in w or '보스턴' in w: form['org'] = 1
	if '@' in w: form['trm'] = 1
	if '개월' in w or bool(re.match('\d+/\d+/\d+', w)) or '요일' in w or '봄' in w or '여름' in w or '가을' in w or '겨울' in w: form['date'] = 1
#	else: form['date'] = 0
	if bool(re.match('.*초', w)) or bool(re.match('^.+분', w)) or bool(re.match('^.+시', w)): form['time'] = 1
#	else: form['time'] = 0
	if '대회' in w or '차전' in w or '챔피언' in w or '월드리그' in w or '유로2008' in w or '올림픽' in w or '결승' in w or '8강' in w or '예선' in w or '브리티시여자오픈' in w or '월드콩그레스' in w: form['event'] = 1
#	else: form['event'] = 0
	if '아메리카' in w or '한국은' in w or '페테르부르크' in w or '필리핀' in w: form['location'] = 1
#	else: form['location'] = 0
	if '1' in w or '2' in w or '3' in w or '4' in w or '5' in w or '6' in w or '7' in w or '8' in w or '9' in w or '0' in w: form['number'] = 1
#	else: form['number'] = 0
	if len(w) > 3 or '!' in w or '에서' in w or ',' in w or '.' in w or bool(re.match('^.*의', w)) or bool(re.match('^.*이', w)) or bool(re.match('.*를', w)): form['sen'] = 1
#	else: form['sen'] = 0
	form['word'] = w
	return form

fp = open('entity_data_utf8.txt', encoding='utf-8')
train = ['\t'.join(fp.readline().split()[1:]) for i in range(1000000)]
test = ['\t'.join(fp.readline().split()[1:]) for i in range(63571)]
fp.close()
fp = open('train.txt', 'w')
t = [fp.write(i+'\n') for i in train]
fp.close()
fp = open('test.txt', 'w')
t = [fp.write(i+'\n') for i in test]
fp.close()
fp = open('train.txt', 'r')
train = [tuple(i.split()) for i in fp.readlines()]
train = [(features(w), t) for (w, t) in train]
fp.close()
fp = open('test.txt', 'r')
test = [tuple(i.split()) for i in fp.readlines()]
test = [(features(w), t) for (w, t) in test]
fp.close()
classifier = nltk.NaiveBayesClassifier.train(train)
print(nltk.classify.accuracy(classifier, test))
