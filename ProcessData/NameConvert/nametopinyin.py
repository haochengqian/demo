
from pypinyin import pinyin, lazy_pinyin,Style
import os
import string

mylist = []
file_obj = open("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/name.txt")
all_lines = file_obj.readlines()
for line in all_lines:
    line = line.strip('\r\n')
    mylist.append(lazy_pinyin(unicode(line,'utf-8')))
file_obj.close()

if os.path.exists("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/nameAfterTrans.txt"):
    os.remove("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/nameAfterTrans.txt")

file_write_obj = open("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/nameAfterTrans.txt",'w')
for item in mylist:
    item.pop()
    file_write_obj.write(' '.join(item).encode("utf-8"))
    file_write_obj.write('\r\n')
file_write_obj.close()