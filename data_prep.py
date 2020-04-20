#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from data_parser.parser import word_parser

with open('zhaoshi.txt', 'r') as f:
    content = f.read().replace('\n', ' ');
    words = list(filter(None, re.split(' |，|,|:|：|、|·|\+|\=', content)))

    look_up_vowel = defaultdict(list)
    look_up_length = defaultdict(list)

    for word in words:
        pinyins = word_parser(word)
        look_up_length[len(word)].append(word)
        if len(word) > 1:
            look_up_vowel[tuple([pinyin[1][-1] for pinyin in pinyins[-2:]])].append(word)
        if len(word) > 2:
            look_up_vowel[tuple([pinyin[1][-1] for pinyin in pinyins[-3:]])].append(word)
        if len(word) > 3 and word[-4] != '，':
            look_up_vowel[tuple([pinyin[1][-1] for pinyin in pinyins[-4:]])].append(word)

with open('zhaoshi_length_dict.txt', 'w', encoding="utf-8") as f:
    for k, v in look_up_length.items():
        f.write('{}\t{}\n'.format(k, ' '.join(sorted(v))))
    print('完成！')

with open('zhaoshi_vowel_dict.txt', 'w', encoding="utf-8") as f:
    for k, v in look_up_vowel.items():
        f.write('{}\t{}\n'.format(' '.join(list(k)), ' '.join(sorted(v))))
    print('完成！')
