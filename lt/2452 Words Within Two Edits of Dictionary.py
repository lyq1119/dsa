from typing import List
from collections import defaultdict
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        mylist = []
        letters = [chr(97+i) for i in range(26)]
        myset = set()
        for word in dictionary:
            for i in range(len(word)):
                for letter in letters:
                    myset.add(word[:i]+letter+word[(i+1):])
        for word in queries:
            flag = False
            for i in range(len(word)):
                for letter in letters:
                    if flag:
                        break
                    if word[:i]+letter+word[(i+1):] in myset:
                        flag = True
                if flag:
                    break
            if flag:
                mylist.append(word)
        return mylist