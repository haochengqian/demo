#-*- coding:utf-8 –*-

import MySQLdb.cursors
from RecognizePinYin import Recognition
from Pinyin2Hanzi import is_pinyin # 判断拼音是否合法

db = MySQLdb.connect("localhost", "root", "haochengqian262", "artical", cursorclass = MySQLdb.cursors.SSCursor)
cursor = db.cursor()

def ReadInfoFromDB():
    with db:
        cursor.execute('select * from dbo_west_zone')
        rows = cursor.fetchall()
        for row in rows:
            if row[3] is None:
                cursor.execute('delete from dbo_west_zone where F_uniqueId = \'%s\'' % row[0])
                db.commit()
                print "delete %s" % row[0]
                continue
            print row[0], row[3]
            nameUnprocess = row[3].replace('-',' ')
            nameUnprocess = nameUnprocess.replace(',',' ')
            nameSet = nameUnprocess.split(';')
            namePinyinFlag = False
            i = 0
            # for i in range(len(nameSet) - 1):
            #     nameSet[i] = seg(nameSet[i])
            #     i += 1
            for name in nameSet:
                name = seg(name)
                if Recognition.Recognition(name) == True:
                    namePinyinFlag = True
                    continue
            if namePinyinFlag == False:
                cursor.execute('delete from dbo_west_zone where F_uniqueId = \'%s\'' % row[0])
                db.commit()
                print "delete %s" % row[0]



def seg(pinyin): # 拼音分词 且可判断是否为拼音
    sm = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z', 'sh', 'zh', 'ch']
    ymd = {'a': {'i':None, 'o':None, 'n': {'g': None}},
           'e': {'i':None, 'r':None, 'n': {'g': None}},
           'i': {'e':None, 'a':{'n':{'g':None}, 'o':None}, 'u':None, 'o':{'n':{'g':None}}, 'n':{'g':None}},
           'o': {'u':None, 'n':{'g':None}},
           'u': {'a':{'i':None, 'n':{'g':None}}, 'e':None, 'i':None, 'o':None}
          }
    result, i = '', 0
    while i < len(pinyin)-1:
        if pinyin[i] in ['s', 'z', 'c'] and pinyin[i+1] == 'h':
            result += ' ' + pinyin[i] + 'h'
            i += 2
        elif pinyin[i] in sm:
            result += ' ' + pinyin[i]
            i += 1
        else:
            if pinyin[i] != ' ':
                result += ' '
        tmp, tmpd = '', ymd
        while i < len(pinyin):
            if pinyin[i] != ' ':
                if tmpd.get(pinyin[i], 0) == 0:
                    print "this is not a pinyin name"
                    return "NOTPINYIN"
                tmpd = tmpd[pinyin[i]]
                tmp += pinyin[i]
            i += 1
            if not (i < len(pinyin) and tmpd and tmpd.has_key(pinyin[i])):
                break
        result += tmp
    return result.strip()



if __name__ == '__main__':
    ReadInfoFromDB()
#    print seg('plone')
    db.close()
    cursor.close()