#-*- coding:utf-8 –*-
import synonyms

sen1 = "机器学习"
sen2 = "深度学习"
r = synonyms.compare(sen1, sen2, seg=True)

print sen1,sen2,r