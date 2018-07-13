#-*- coding:utf-8 –*-

import MySQLdb.cursors
from RecognizePinYin import Recognition
from Pinyin2Hanzi import is_pinyin
from ProcessData import KeywordExtraction
from HMM.hmm.Input import input

db = MySQLdb.connect("localhost", "root", "haochengqian262", "artical", cursorclass = MySQLdb.cursors.SSCursor)
cursor = db.cursor()

def ReadInfoFromDB():
    with db:
        cursor.execute('select * from dbo_west_zone limit 5')
        rows = cursor.fetchall()
        name = ""
        Assio = ""
        keyWord = ""
        for row in rows:
            if row[6] is not None:
                keyWord = row[6]
            else:
                keyWord = KeywordExtraction.keyWordExtraction(row[5])

            name = row[3]
            Assio = row[11]
            print name
            print Assio
            print keyWord

            input(name, keyWord, Assio, ";")




if __name__ == '__main__':
    ReadInfoFromDB()
    db.close()
    cursor.close()