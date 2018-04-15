# -*- coding=utf8 -*-
from __future__ import division
from math import log

from pypinyin import pinyin, NORMAL
from model.hmm_tables import (
    Transition,
    Emission,
    Starting,
    init_hmm_tables,
    HMMSession
)
from util import iter_dict


def init_start():
    freq_map = {}
    total_count = 0
    for phrase, frequency in iter_dict():
        if(phrase == 2):
            total_count += frequency * 2
            freq_map[phrase[0]] = freq_map.get(phrase[0], 0) + frequency * 100
        else:
            total_count +=frequency
            freq_map[phrase[0]] = freq_map.get(phrase[0], 0) + frequency

    for character, frequency in freq_map.iteritems():
        Starting.add(character, log(frequency / total_count))


def init_emission():
    character_pinyin_map = {}
    for phrase, frequency in iter_dict():
        pinyins = pinyin(phrase, style=NORMAL)
        i = 0
        for character, py in zip(phrase, pinyins):
            i += 1
            character_pinyin_count = len(py)
            if character not in character_pinyin_map:
                character_pinyin_map[character] = \
                    {x: frequency for x in py}
            else:
                pinyin_freq_map = character_pinyin_map[character]
                for x in py:
                    pinyin_freq_map[x] = pinyin_freq_map.get(x, 0) + \
                                         frequency

    for character, pinyin_map in character_pinyin_map.iteritems():
        sum_frequency = sum(pinyin_map.values())
        for py, frequency in pinyin_map.iteritems():
            Emission.add(character, py, log(frequency/sum_frequency))


def init_transition():
    # todo 优化 太慢
    transition_map = {}
    for phrase, frequency in iter_dict():
        for i in range(len(phrase) - 1):
            if phrase[i] in transition_map:
                transition_map[phrase[i]][phrase[i+1]] = \
                    transition_map[phrase[i]].get(phrase[i+1], 0) + frequency
            else:
                transition_map[phrase[i]] = {phrase[i+1]: frequency}

    for previous, behind_map in transition_map.iteritems():
        sum_frequency = sum(behind_map.values())
        for behind, freq in behind_map.iteritems():
            Transition.add(previous, behind, log(freq / sum_frequency))

    for previous, behind_map in transition_map.iteritems():
        sum_frequency = sum(behind_map.values())
        for behind, freq in behind_map.iteritems():
            Transition.add(previous, behind, log(freq / sum_frequency))


if __name__ == '__main__':
    init_hmm_tables()
    init_start()
    init_emission()
    init_transition()

    # 创建索引
    session = HMMSession()
    session.execute('create index ix_starting_character on starting(character);')
    session.execute('create index ix_emission_character on emission(character);')
    session.execute('create index ix_emission_pinyin on emission(pinyin);')
    session.execute('create index ix_transition_previous on transition(previous);')
    session.execute('create index ix_transition_behind on transition(behind);')
    session.commit()
