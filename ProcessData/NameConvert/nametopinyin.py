
from pypinyin import pinyin, lazy_pinyin,Style
import os
import string

mylist = []
file_obj = open("/Users/mac/Downloads/Chinese-Names-Corpus-master/Chinese_Names_Corpus.txt")
all_lines = file_obj.readlines()
for line in all_lines:
    line = line.strip('\r\n')
    mylist.append(lazy_pinyin(unicode(line,'utf-8'),style=Style.TONE2))
file_obj.close()

if os.path.exists("/Users/mac/Documents/data/namepinyin.txt"):
    os.remove("/Users/mac/Documents/data/namepinyin.txt")

file_write_obj = open("/Users/mac/Documents/data/namepinyin.txt",'w')
for item in mylist:
    file_write_obj.write(' '.join(item).encode("ascii"))
    file_write_obj.write('\r\n')
file_write_obj.close()