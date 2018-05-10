#-*- coding:utf-8 –*-

import synonyms
import MySQLdb

from SocialNet.socialNet import Scholar, RelationShip, init_socialNet_tables

class WordDisambiguation:
    userAndKeyword = {}
    userAndAssosiation = {}
    def __init__(self):
        self.userAndKeyword.clear()
        self.userAndAssosiation.clear()
        self.readPersonFromDB()

    def addKey(self, key, value):
        if self.userAndKeyword.has_key(key) == False:
            self.userAndKeyword[key] = []
        else:
            self.userAndKeyword[key].append(value)

    def getVal(self, key):
        return self.userAndKeyword[key]

    def compareWord(self, wordA, wordB):
        result = synonyms.compare(wordA, wordB, seg=True)
        return result

    def comparePerson(self, name, wordA):
        if self.userAndKeyword.has_key(name) == False:
            return 0
        count = 0.0
        for i in wordA:
             t = self.userAndKeyword[name]
             for s in t:
                if self.compareWord(i, s) > 0.5 :
                    count += 1
                    break
        count /= len(wordA)
        return count

    def addAssos(self, key, value):
        if self.userAndAssosiation.has_key(key) == False:
            self.userAndAssosiation[key] = []
        else:
            self.userAndAssosiation[key].append(value)

    def getAssos(self, key):
        return self.userAndAssosiation[key]

    def readPersonFromDB(self):
        init_socialNet_tables()
        db = MySQLdb.connect("localhost", "root", "haochengqian262", "name")
        cursor = db.cursor()
        cursor.execute("select * from keyword2")
        rows = cursor.fetchall()
        nameId = 1
        for row in rows:
            value = row[2].replace(' ', '')
            value = value.split('||')
            name = row[0].replace(' ', '')
            name = name.split('||')
            department = row[5].replace(' ', '')
            department = department.replace('||', ' ')
            assosiation = row[4] + "\n " + row[5] + "\n"
            # TODO add name compare. delete some same person
            for wordA in name:
                #print nameId, wordA, row[4], row[5]
                # Scholar.add(nameId, wordA.decode('utf8', 'ignore'), \
                #             str(row[4]).decode('utf8', 'ignore'), \
                #             department.decode('utf8', 'ignore'))
                relation = ""
                for i in range (len(wordA)):
                    relation += str(nameId) + "||"
                # RelationShip.add(nameId, relation)
                for wordB in value:
                    self.addKey(wordA, wordB)
                    self.addAssos(wordA, assosiation)

                nameId += 1







