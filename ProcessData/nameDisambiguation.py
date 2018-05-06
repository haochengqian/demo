import MySQLdb
import sys
import synonyms

reload(sys)
sys.setdefaultencoding('utf8')

db = MySQLdb.connect("localhost","root","haochengqian262","name")
db2 = MySQLdb.connect("localhost", "root","haochengqian262", "afterTranslate")
cursor = db.cursor()
cursor2 = db2.cursor()

#f = open('/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/keyword', 'w')

if __name__ == '__main__':
    cursor.execute("select * from keyword2")
    rows = cursor.fetchall()
    cursor2.execute("s")
    for row in rows:
        i = 0
        for r in row:
            i += 1
            if i != 4:
                r = r.replace("||"," ")
            f.write(r + '\n')
        f.write('\n')

    cursor.close()
    f.close()