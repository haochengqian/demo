from nlp_rake import rake
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = MySQLdb.connect("localhost","root","haochengqian262","artical")
cursor = db.cursor()


# keywords = rake_object.run(text)

# print("Keywords:", keywords)

if __name__ == '__main__':
    cursor.execute("select * from dbo_west_zone limit 2,2;")
    rows = cursor.fetchall()
    stoppath = 'SmartStoplist.txt'
    rake_object = rake.Rake(stoppath)
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
        keywords = rake_object.run(row[5])
        print keywords
    cursor.close()
    db.close()