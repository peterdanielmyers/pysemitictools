#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
from unicodedata import *

head = u'''#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

with io.open('hebrew_dict.py', 'w', encoding='utf-8') as file:
    start = 1425
    end = 1524
    i = start
    file.write(head)
    file.write(u'hebrew = {')
    while i <= end:
        try:
            file.write(u"\tu'"+name(unichr(i))+u"' : u'"+unichr(i)+u"', \n")
        except ValueError:
            print unichr(i) + u' is not a unicode char with a name.'
        i += 1
    file.write(u'}\n')