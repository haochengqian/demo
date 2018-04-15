# -*- coding=utf8 -*-
import os
from model.hmm_tables import Emission, Transition
name_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/familyname')

phra = set()
def iter_name():
    with open(name_path, 'r', ) as t:
        for line in t:
            phra.add(line.replace('\n','').decode('utf8'))

def viterbi(pinyin_list):
    start_char = Emission.join_starting(pinyin_list[0])
    iter_name()
    family_name = phra
    V = {}
    for char, prob in start_char:
        if char in family_name:
            V[char] = prob

    for i in range(1, len(pinyin_list)):
        pinyin = pinyin_list[i]

        prob_map = {}
        for phrase, prob in V.iteritems():
            character = phrase[-1]
            result = Transition.join_emission(pinyin, character)
            if not len(result):
                continue

            for state, new_prob in result:
                prob_map[phrase + state] = new_prob + prob

        if prob_map:
            V = prob_map
        else:
            return V
    return V


if __name__ == '__main__':
    while 1:
        string = raw_input('input:')
        pinyin_list = string.split()
        V = viterbi(pinyin_list)

        for phrase, prob in sorted(V.items(), key=lambda d: d[1], reverse=True):
            print phrase, prob
