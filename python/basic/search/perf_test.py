#!/usr/bin/env python3

import time
import timeit

from bf_search import search

text = 'Peter told me that Peter the pickle piper piped a pitted pickle before he petered out. Phew!j;lasjfl;ajfweoqfjofjas;fjsfjofjjaf;fljasfl;jgoweijtfoajfsa;gfjsgherpigtfu9wt5u4985tugh;sdfj;aghafja;fkwqp[r4231i0jfagasff;sajf Peterjfksdjfl'*100000

sub_text = 'Peter'

t1 = time.time()
for _ in range(0,10):
    [i for i in search(text,sub_text)]

print("quick_search cost time = {}s".format(int(time.time()-t1)))