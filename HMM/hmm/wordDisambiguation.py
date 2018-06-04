#-*- coding:utf-8 –*-

import synonyms
import MySQLdb
#from Synonym.Hybrid_Sim import HybridSim

from SocialNet.socialNet import Scholar, RelationShip, init_socialNet_tables

class WordDisambiguation:
    userAndKeyword = {}
    userAndAssosiation = {}
    db = MySQLdb.connect("localhost", "root", "haochengqian262", "journal_all")
    cursor = db.cursor()
    def __init__(self):
        self.userAndKeyword.clear()
        self.userAndAssosiation.clear()
        self.readPersonFromDB()
        self.db = MySQLdb.connect("localhost", "root", "haochengqian262", "journal_all")
        self.cursor = self.db.cursor()

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
                # print i,s," ",
                # print s," "
                if self.compareWord(i, s) > 0.5 :
                    count += 1
                    break
                # elif HybridSim.get_Final_sim(i, s) > 0.5 :
                #     count += 1
                #     break
        count /= len(wordA)
        return count

    def compareAssios(self, assios1, assios2):
        return self.compareWord(assios1, assios2)

    def addAssos(self, key, value):
        if self.userAndAssosiation.has_key(key) == False:
            self.userAndAssosiation[key] = []
            self.userAndAssosiation[key].append(value)
        else:
            self.userAndAssosiation[key].append(value)

    def getAssos(self, key):
        return self.userAndAssosiation[key]

    def compareFriend(self, name, assio):
        resList = set()
        self.cursor.execute("select author_cn from journal_all_17_30"
                            " where first_authors_cn = \'%s\' "
                            "AND organizations_simple_cn = "
                             % name + "'" + assio + "'")
        rows = self.cursor.fetchall()
        for row in rows:
            nameList = row[0].split('||')
            for n in nameList:
                # print n,
                resList.add(n)
        return resList

    def readPersonFromDB(self):
        init_socialNet_tables()
        self.cursor.execute("select * from journal_all_17_30")
        rows = self.cursor.fetchall()
        nameId = 1
        for row in rows:
            value = row[19].replace(' ', '')
            value = value.split('||')
            name = row[9].replace(' ', '')
            name = name.split('||')
            department = row[11].replace(' ', '')
            department = department.replace('||', ' ')
            assosiation = row[12] + "\n"
            # TODO add name compare. delete some same person
            for wordA in name:
                # # print nameId, wordA, row[4], row[5]
                # Scholar.add(nameId, wordA.decode('utf8', 'ignore'), \
                #             str(row[4]).decode('utf8', 'ignore'), \
                #             department.decode('utf8', 'ignore'))
                # relation = ""
                # for i in range (len(wordA)):
                #     relation += str(nameId) + "||"
                # RelationShip.add(nameId, relation)
                for wordB in value:
                    self.addKey(wordA, wordB)
                self.addAssos(wordA, assosiation)
                nameId += 1







