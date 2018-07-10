# -*- coding=utf8 -*-

import os
from googletrans import Translator
from HMM.hmm.viterbi import viterbi
from wordDisambiguation import WordDisambiguation
from pypinyin import pinyin, NORMAL

name_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/familyname')

translator = Translator(['translate.google.cn'])

def input(name, keyWord, Assio, separator = '||'):  # viterbi 输入接口
    wordDis = WordDisambiguation()
    name = name.replace('-',' ')
    name = name.lower()
    name = name.split(separator)

    keyWordList = keyWord.split(separator)
    keyWord = []
    i = 0
    for kw in keyWordList:  # 翻译关键字
        word = translator.translate(kw, dest='zh-cn', src='en').text
        print word + ""
        keyWord.append(word.encode('utf-8'))
        print ""

    Assio = translator.translate(Assio)

    print Assio

    authorFirst = name[0]
    pinyin_list = authorFirst.split(' ')
    pinyinAll = ""
    for ph in pinyin_list:
        pinyinAll += ph
    V = viterbi(pinyinAll)  # viterbi搜索结果

    author_prob = {}
    for phrase, prob in V.iteritems(): # 根据百家姓剔除结果
        pinyinFound = ""
        namePinyin = pinyin(phrase, style=NORMAL)
        for n in namePinyin:
            for t in n:
                pinyinFound += t.encode("utf8")
        if cmp(pinyinFound[0:len(pinyinAll)], pinyinAll) != 0:
            continue
        author_prob[phrase] = prob

    nameSet = {}
    author_prob = sorted(author_prob.items(), key=lambda item: item[1],reverse=True)

    for phrase, prob in author_prob:
        result = wordDis.comparePerson(phrase.encode("utf8", keyWord))
        if result > (0.8 / len(keyWord)):
            print "找到了标签相同的名字： "
            assois = wordDis.getAssos(phrase.encode("utf8"))
            nameSet[phrase] = assois
            print phrase, prob

    DeleteList = []

    for name, position in nameSet.iteritems():
        deleteFlag = True
        for key in position:
            # print key,Assio
            key = key.replace('\n', '')
            key = key.replace('||', ' ')
            if wordDis.compareAssios(Assio, key) > 0.6:
                print "找到了单位相同的名字： %s" % name
                deleteFlag = False
                break
        if deleteFlag:
            print "%s 该名字单位有误" % name
            DeleteList.append(name)

    for name in DeleteList:
        nameSet.pop(name)

    for name, position in nameSet.iteritems():
        nameList = wordDis.compareFriend(name, Assio)
        for otherName in author:
            # print otherName,
            flag = False
            for compareName in nameList:
                # print compareName
                pinyinCompareName = pinyin(compareName.decode('utf8'), NORMAL)
                pinyinList = []
                for key in pinyinCompareName:
                    pinyinList.append(key[0])
                pinyinCompareName = " ".join(pinyinList)
                # print pinyinCompareName
                pinyinCompareName.encode('utf8')
                if otherName == pinyinCompareName:
                    flag = True
                    print "找到了学术圈相同的名字： %s" % name
            if not flag:
                print "未找到以 %s老师 为第一作者的信息" % name


if __name__ == '__main__':

    wordDis = WordDisambiguation()
    while True:
        author = raw_input('请输入作者拼音名字以||分隔：')
        # title = raw_input('请输入题目以||分隔：')
        # brief = raw_input('请输入摘要以||分隔：')
        keyWord = raw_input('请输入关键词以||分隔：')
        Assio = raw_input('请输入单位以||分隔：')

        author = author.replace('-', ' ')
        author = author.lower()
        author = author.split('||')

        keyWordList = keyWord.split('||')
        keyWord = []
        i = 0
        for kw in keyWordList:
            word = translator.translate(kw, dest='zh-cn', src='en').text
            print word+" ",
            keyWord.append(word.encode('utf-8'))
            print ""

        # title = translator.translate(title, dest='zh-cn', src='en').text.encode('utf-8')
        # brief = translator.translate(brief, dest='zh-cn', src='en').text.encode('utf-8')
        Assio = translator.translate(Assio, dest='zh-cn', src='en').text.encode('utf-8')

        print Assio

        authorFirst = author[0]

        pinyin_list = authorFirst.split(' ')
        pinyinAll = ""
        for ph in pinyin_list:
            pinyinAll += ph
        V = viterbi(pinyin_list)

        author_prob = {}

        for phrase, prob in V.iteritems():
            pinyinFound = ""
            namePinyin = pinyin(phrase, style=NORMAL)
            for n in namePinyin:
                for t in n:
                    pinyinFound += t.encode("utf8")
            if cmp(pinyinFound[0:len(pinyinAll)], pinyinAll) != 0:
                continue
            author_prob[phrase] = prob

        nameSet = {}
        author_prob = sorted(author_prob.items(), key=lambda item: item[1],reverse=True)
        for phrase, prob in author_prob:
            result = wordDis.comparePerson(phrase.encode("utf8"), keyWord)
            if result > (0.8 / len(keyWord)):
                print "找到了标签相同的名字： "
                assois = wordDis.getAssos(phrase.encode("utf8"))
                # for key in assois:
                #     print key
                # print "结果：" + str(result)
                nameSet[phrase] = assois
                print phrase, prob
            # else:
                 # print "此人不在行列内." + phrase + str(prob)

        DeleteList = []

        for name, position in nameSet.iteritems():
            deleteFlag = True
            for key in position:
                # print key,Assio
                key = key.replace('\n','')
                key = key.replace('||', ' ')
                if wordDis.compareAssios(Assio, key) > 0.6:
                    print "找到了单位相同的名字： %s" % name
                    deleteFlag = False
                    break
            if deleteFlag:
                print "%s 该名字单位有误" % name
                DeleteList.append(name)

        for name in DeleteList:
            nameSet.pop(name)

        for name, position in nameSet.iteritems():
            nameList = wordDis.compareFriend(name,Assio)
            for otherName in author:
                # print otherName,
                flag = False
                for compareName in nameList:
                    # print compareName
                    pinyinCompareName = pinyin(compareName.decode('utf8'), NORMAL)
                    pinyinList = []
                    for key in pinyinCompareName:
                        pinyinList.append(key[0])
                    pinyinCompareName = " ".join(pinyinList)
                    # print pinyinCompareName
                    pinyinCompareName.encode('utf8')
                    if otherName == pinyinCompareName:
                        flag = True
                        print "找到了学术圈相同的名字： %s" % name
                if not flag:
                    print "未找到以 %s老师 为第一作者的信息" % name







