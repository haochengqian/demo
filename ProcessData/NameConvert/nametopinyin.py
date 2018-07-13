
from pypinyin import pinyin, lazy_pinyin,Style
import os
import string

mylist = []
file_obj = open("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/familyname")
all_lines = file_obj.readlines()
for line in all_lines:
    line = line.strip('\r\n')
    mylist.append(lazy_pinyin(unicode(line,'utf-8')))
file_obj.close()

if os.path.exists("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/nameAfterTransFamilyName.txt"):
    os.remove("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/nameAfterTransFamilyName.txt")

file_write_obj = open("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/nameAfterTransFamilyName.txt",'w')
mylist2 = []
for item in mylist:
    if item not in mylist2:
        mylist2.append(item)
mylist2.sort()
for item in mylist2:
#    item.pop()
    file_write_obj.write(' '.join(item).encode("utf-8"))
    file_write_obj.write('\r\n')
file_write_obj.close()