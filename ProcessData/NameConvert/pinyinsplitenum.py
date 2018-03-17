from pypinyin import pinyin, lazy_pinyin,Style
import os
import string

mylist = []
file_obj = open("/Users/mac/Documents/data/namepinyin.txt")
all_lines = file_obj.readlines()

for line in all_lines:
    t = line.replace('1','')
    t = t.replace('2','')
    t = t.replace('3','')
    t = t.replace('4','')
    t = t.replace('\r\n','')
    mylist.append(t)
file_obj.close()

#if os.path.exists("/Users/mac/Documents/data/namepinyinnonum.txt"):
#    os.remove("/Users/mac/Documents/data/namepinyinnonum.txt")

file_write_obj = open("/Users/mac/Documents/data/namepinyinnonum.txt",'w')
for item in mylist:
    file_write_obj.write(''.join(item))
    file_write_obj.write('\r\n')
file_write_obj.close()