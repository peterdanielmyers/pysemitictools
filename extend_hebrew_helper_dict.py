#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
from hebrew_dict import *
import itertools

head = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

new_hebrew_dict = {}
collection_dict = {}

# Organise the characters by type according to their names
for key, item in hebrew.iteritems():
    key_words = key.split(u' ')
    key_words = key_words[1:] # Get rid of "Hebrew" at the beginning of each name
    if not key_words[0] in collection_dict:
        collection_dict[key_words[0]] = []
    collection_dict[key_words[0]].append((key_words[1:],item))

with io.open('hebrew_dict.py', 'w', encoding='utf-8') as file:
    file.write(head)
    file.write(u'hebrew = {\n')
    for key, value in hebrew.iteritems():
        file.write(u"\tu'"+key+u"' : u'"+value+u"', \n")
    file.write(u'}\n')
    for key, collection in collection_dict.iteritems():
        file.write(key+u' = {\n')
        for item in collection:
            file.write(u'\tu"'+u' '.join(item[0])+u'" : u"'+item[1]+u'",\n')
        file.write(u'}\n')