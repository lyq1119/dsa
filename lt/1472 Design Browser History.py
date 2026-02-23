class Node:
    def __init__(self,val=None,val1=None,val2=None):
        self.prev = val1
        self.next = val2
        self.val = val
class BrowserHistory:
    def __init__(self, homepage: str):
        homepage = Node(homepage)
        self.cur = homepage
    def visit(self, url: str) -> None:
        cururl = Node(url)
        self.cur.next = cururl
        cururl.prev = self.cur
        self.cur = cururl
    def back(self, steps: int) -> str:
        while self.cur.prev and steps:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val
    def forward(self, steps: int) -> str:
        while self.cur.next and steps:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
