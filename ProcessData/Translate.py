# -*- coding:utf-8 –*-

import MySQLdb.cursors
import time
from googletrans import Translator
from pypinyin import pinyin, NORMAL

file_obj = open("/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/testData.txt",'w+')

db = MySQLdb.connect("localhost", "root", "haochengqian262", "journal_all")

cursor = db.cursor()

translator = Translator(['translate.google.cn'])

row_list = {
    'id': 0, 'source_url': 1, 'title_cn': '2', 'title_en': '3',
    'brief_cn': 4, 'brief_en': 5, 'classification_s': 6,
    'doi_s': 7, 'author_cn': 8, 'author_en': 9,
    'organization_each_cn': 10, 'organization_simple_cn': 11,
    'organization_detail_cn': 12, 'first_authors_cn': 13,
    'journal_cn': 14, 'journal_en': 15, 'year_s': 16,
    'issue_s': 17, 'keyword_cn': 18, 'keyword_en': 19,
    'publication_date': 20, 'found_cn': 21
}


def trans(row):
    id = row[0]
    author = translator.translate(row[9]).text.encode('utf8')
    keyword = translator.translate(row[19]).text.encode('utf8')
    assio = translator.translate(row[12]).text.encode('utf8')
    file_obj.write(id + ' ' + author + ' ' + keyword + ' ' + assio + '\r\n')
    db.commit()
    time.sleep(0.16)


def get_Row_name():
    with db:
        cursor.execute('select * from journal_all_17_30 limit 15000,18000')

        rows = cursor.fetchall()
        count = 0
        for row in rows:
            count = count + 1
            print "this item is " + str(count)
            trans(row)


def close_connection():
    cursor.close();
    db.close()
    file_obj.close()


if __name__ == '__main__':
    get_Row_name()
    close_connection()

