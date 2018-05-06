#-*- coding:utf-8 –*-

import synonyms

sen1 = "同年"
sen2 = "同龄"
r = synonyms.compare(sen1, sen2, seg=False)

print r;

class WordDisambiguation:
    userAndKeyword = {}
    def __init__(self):
        self.userAndKeyword.clear()

    def addKey(self, key, value):
        self.userAndKeyword[key] = []
        self.userAndKeyword[key].append(value)

    def getVal(self, key):
        return self.userAndKeyword[key]

    def compareWord(self, wordA, wordB):
        result = synonyms.compare(wordA, wordB)
        return result

    





