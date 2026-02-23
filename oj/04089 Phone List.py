class Trie:
    def __init__(self):
        self.tree = {}
    def insert(self, word: str) -> None:
        cur = self.tree
        for i in range(len(word)-1):
            a = word[i]
            if a in cur:
                cur = cur[a]
            else:
                cur[a] = {}
                cur = cur[a]
        if word[-1] in cur:
            cur = cur[word[-1]]
            cur[None] = {}
        else:
            cur[word[-1]] = {None:{}}
    def startsWith(self, prefix: str) -> bool:
        cur = self.tree
        for t in list(prefix):
            if t not in cur:
                return False
            cur = cur[t]
        return True
for _ in range(int(input())):
    n = int(input())
    phonenumbers = []
    for __ in range(n):
        phonenumbers.append(input())
    phonenumbers.sort(key=lambda x:len(x),reverse=True)
    trie = Trie()
    flag = True
    for number in phonenumbers:
        if trie.startsWith(number):
            flag = False
            break
        trie.insert(number) 
    if flag:
        print("YES")
    else:
        print("NO")       