n = int(input())
from collections import deque
class Word:
    def __init__(self,word):
        self.word = word
        self.previous = None
        self.neighbors = set()
        self.color = 0
class Graph:
    def __init__(self):
        self.vertices = {}
        self.daxiaoxie = 0
    def add_edge(self,worda,wordb):#worda和wordb是vertice对象
        worda.neighbors.add(wordb)
        wordb.neighbors.add(worda)
    def add_edges(self):
        if self.daxiaoxie == 0:
            for aword in self.vertices:
                worda = self.vertices[aword]
                awordlist = list(aword)
                for i in range(4):
                    l = awordlist[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c != l:
                            awordlist[i] = c
                            newword = "".join(awordlist)
                            if newword in self.vertices:
                                self.add_edge(worda,self.vertices[newword])
                    awordlist[i] = l    
        else:
            for aword in self.vertices:
                worda = self.vertices[aword]
                awordlist = list(aword)
                for i in range(4):
                    l = awordlist[i]
                    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        if c != l:
                            awordlist[i] = c
                            newword = "".join(awordlist)
                            if newword in self.vertices:
                                self.add_edge(worda,self.vertices[newword])
                    awordlist[i] = l
mygraph = Graph()
for _ in range(n):
    word = input()
    if word[0] not in "abcdefghijklmnopqrstuvwxyz":
        mygraph.daxiaoxie = 1
    mygraph.vertices[word] = Word(word)
mygraph.add_edges()
begin,end = input().split()
begin = mygraph.vertices[begin]
end = mygraph.vertices[end]
def bfs(begin,end):
    queue = deque([begin])
    begin.color = 1
    while queue:
        word = queue.popleft()#word是对象
        if word == end:
            return word
        for neiword in word.neighbors:
            if neiword.color == 0:
                neiword.color = 1
                neiword.previous = word
                queue.append(neiword)
word = bfs(begin,end)
if not word:
    print("NO")
else:
    current = end
    result = []
    while current.previous:
        result.append(current.word)
        current = current.previous
    result.append(begin.word)
    result.reverse()
    print(*result)