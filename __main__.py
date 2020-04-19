#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from collections import defaultdict
from data_parser.parser import word_parser
from typing import Set, List, Dict

zhaoshi_vowel_dict = {}
with open('zhaoshi_vowel_dict.txt', 'r', encoding="utf-8") as f:
    for line in f:
        items = line.strip().split('\t')
        zhaoshi_vowel_dict[tuple(items[0].split())] = items[1].split()

zhaoshi_len_dict = {}
with open('zhaoshi_len_dict.txt', 'r', encoding="utf-8") as f:
    for line in f:
        items = line.strip().split('\t')
        zhaoshi_len_dict[int(items[0])] = items[1].split()

def main():
    word1 = input('◼︎ 请输入第一个关键词（默认：惊雷）: ') or '惊雷'
    word2 = input('◼︎ 请输入第二个关键词（默认：紫电）: ') or '紫电'
    word3 = input('◼︎ 请输入第三个关键词（默认：乌云）: ') or '乌云'
    word4 = input('◼︎ 请输入一句诗句（默认：多情自古空余恨）: ') or '多情自古空余恨'

    line1 = '{}，这{}，'.format(word1,
        ''.join(gen_words_with_pattern(word1, [4, 4, 3])))
    line2 = '{}，我{}，'.format(word2,
        ''.join(gen_words_with_pattern(word1, [4, 4, 3])))
    line3 = '{}，它{}，'.format(word3,
        ''.join(gen_words_with_pattern(word1, [4, 5])))
    line4 = '{}，我自手持{}!'.format(word4,
        choice(get_zhaoshi_by_vowel(word4)[3]))
    
    print('\n...生成中...\n')

    song = '\n'.join([line1, line2, line3, line4])
    print(song);

def gen_words_with_pattern(word, breakdowns):
    z = get_zhaoshi_by_vowel(word)
    return [choice(z[b]) for b in breakdowns]


def get_zhaoshi_by_vowel(target_word):
    num_char = len(target_word)
    pinyins = word_parser(target_word)

    zhaoshi = defaultdict(list)

    target_vowel = pinyins[-1][1][-1]
    for k, v in zhaoshi_vowel_dict.items():
        if k[-1] == target_vowel:
            for word in v:
                word_pys = word_parser(word)
                if word[-1] != target_word[-1] \
                        and word not in zhaoshi[len(word)]:
                    zhaoshi[len(word)].append(word)
    return zhaoshi

def get_zhaoshi_by_len(len):
    return choice(zhaoshi_len_dict[len])

if __name__ == '__main__':
    main()
