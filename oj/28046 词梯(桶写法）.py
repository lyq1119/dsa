n = int(input())
from collections import deque
class Word:
    def __init__(self,word):
        self.word = word
        self.previous = None
        self.neighbors = set()
        self.color = 0
bucket = {}
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_edge(self,worda,wordb):#worda和wordb是vertice对象
        worda.neighbors.add(wordb)
        wordb.neighbors.add(worda)
    def add_edges(self):
        for biaoqian in bucket:
            wordset = bucket[biaoqian]
            for worda in wordset:
                for wordb in wordset:
                    if wordb != worda:
                        self.add_edge(self.vertices[worda],self.vertices[wordb])
mygraph = Graph()
for _ in range(n):
    word = input()
    for i in range(len(word)):
        tag = word[:i]+"_"+word[(i+1):]
        bucket.setdefault(tag,set()).add(word)
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