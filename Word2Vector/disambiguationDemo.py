#-*- coding:utf-8 –*-
import synonyms

sen1 = "西藏大学农牧学院,西藏林芝,860000"
sen2 = "西藏大学"
r = synonyms.compare(sen1, sen2, seg=True)

print sen1,sen2,r