import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = MySQLdb.connect("localhost","root","haochengqian262","name")
cursor = db.cursor()

if __name__ == '__main__':
    cursor.execute("select * from keyword2")
    