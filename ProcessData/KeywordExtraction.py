from nlp_rake import rake
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = MySQLdb.connect("localhost","root","haochengqian262","artical")
cursor = db.cursor()

# stoppath = 'data/stoplists/SmartStoplist.txt'
#
# rake_object = rake.Rake(stoppath, 5, 3, 4)
#
# sample_file = open("data/docs/fao_test/w2167e.txt", 'r', encoding="iso-8859-1")
# text = sample_file.read()
#
# keywords = rake_object.run(text)

# 3. print results
#print("Keywords:", keywords)

if __name__ == '__main__':
    cursor.execute("select * from dbo_west_zone limit 1;")
    rows = cursor.fetchall()
    cursor.close()
    db.close()