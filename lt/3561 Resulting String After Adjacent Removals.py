class Solution:
    def resultingString(self, s: str) -> str:
        if not s:
            return s
        adjacent_pairs = {
        'ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij',
        'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs',
        'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz', 'za',
        'ba', 'cb', 'dc', 'ed', 'fe', 'gf', 'hg', 'ih', 'ji',
        'kj', 'lk', 'ml', 'nm', 'on', 'po', 'qp', 'rq', 'sr',
        'ts', 'ut', 'vu', 'wv', 'xw', 'yx', 'zy', 'az'
        }
        check = 0
        mystr = []
        while check <= len(s)-1:
            if mystr and mystr[-1]+s[check] in adjacent_pairs:
                mystr.pop()
                check += 1
                continue
            mystr.append(s[check])
            check += 1
        return "".join(mystr)
