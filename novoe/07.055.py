#!/usr/bin/env python
# -*- coding: Utf-8 -*-
from igra_s_bukv import*
from string import*



s = input("Введите слово для поиска: ")
s = s.decode('utf-8')
g = gen_some_sent()




print(g.count(s))

