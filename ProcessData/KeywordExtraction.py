from nlp_rake import rake
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = MySQLdb.connect("localhost","root","haochengqian262","afterTranslate")
cursor = db.cursor()


# keywords = rake_object.run(text)

# print("Keywords:", keywords)

if __name__ == '__main__':
    cursor.execute("select * from journal_all_1_5 limit 1;")
    rows = cursor.fetchall()
    stoppath = 'SmartStoplist.txt'
    #rake_object = rake.Rake(stoppath)
    for row in rows:
        # sentenceList = rake.split_sentences(row[5])
        # stopwordpattern = rake.build_stop_word_regex(stoppath)
        # phraseList = rake.generate_candidate_keywords(sentenceList,stopwordpattern,stoppath)
        # wordscores = rake.calculate_word_scores(phraseList)
        # keywordcandidates = rake.generate_candidate_keyword_scores(phraseList,wordscores)
        # sortedKeywords = sorted(keywordcandidates.iteritems(),reverse=True)
        # keywords = len(sortedKeywords)
        # for keyword in sortedKeywords[0:(keywords/3)]:
        #     print "Keyword:", keyword[0], ", score:", keyword[1]
        #keywords = rake_object.run(row[5])
        for key in row:
            key = key.replace('.','.\n')
            key = key.replace(';',';\n')
            print key
    cursor.close()
    db.close()