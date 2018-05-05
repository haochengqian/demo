import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = MySQLdb.connect("localhost","root","haochengqian262","name")
cursor = db.cursor()

f = open('/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/keyword', 'w')

if __name__ == '__main__':
    cursor.execute("select * from keyword2")
    rows = cursor.fetchall()
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