#!/usr/bin/env python3

import numpy as np
import pandas as pd

import math
import os
import random
import re
import sys
import json

import pandas as pd

class Rare:

    @staticmethod
    def nth_most_rare(elements, n):

        data = pd.DataFrame([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5,5], columns=['number'])

        # data1 = data.groupby('number').count()
        data1 = data['number'].value_counts()

        data1.sort_values(inplace=True)




        print(data1, type(data1))

print(Rare.nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))
