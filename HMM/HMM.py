#-*-coding:utf-8 -*-
import finalseg
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

sentence_list = [
u"姚晨和老凌离婚了",
u"他说的确实在理",
u"长春市长春节讲话"
]

print u"=默认效果"

for sentence in sentence_list:
	seg_list = finalseg.cut(sentence)
	print "/ ".join(seg_list)

print u"\n=打开新词发现功能后的效果\n"


for sentence in sentence_list:
	seg_list = finalseg.cut(sentence,find_new_word=True)
	print "/ ".join(seg_list)