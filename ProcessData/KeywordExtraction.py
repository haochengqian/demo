from nlp_rake import rake

# keywords = rake_object.run(text)

# print("Keywords:", keywords)

def keywordExtraction(Abstract):
    stopPath = 'SmartStoplist.py'
    rake_object = rake.Rake(stopPath)
    sentenceList = rake.split_sentences(Abstract)
    stopWordPattern = rake.build_stop_word_regex(stopPath)
    phraseList = rake.generate_candidate_keywords(sentenceList, stopWordPattern, stopPath)
    wordScores = rake.calculate_word_scores(phraseList)
    keywordCandidates = rake.generate_candidate_keyword_scores(phraseList, wordScores)
    sortedKeywords = sorted(keywordCandidates.iteritems(), reverse=True)
    return sortedKeywords