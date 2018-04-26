#-*- coding:utf-8 –*-

import xlwt
import StringIO

file = open('data')
alllines = file.readlines()

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('mysheet',cell_overwrite_ok=True)
i = 0
for line in alllines:
    j = 0
    t = line.replace('\n','')
    t = t.replace(',','')
    word = t.split(' ')
    for w in word:
        sheet.write(i,j,w)
        if(w == '' or w == '\n'):
            continue
        j+=1
        print w
    i+=1
book.save('test.xls')