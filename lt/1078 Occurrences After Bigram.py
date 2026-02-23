class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        text = text.split()
        mylist = []
        for i in range(len(text)):
            if i < len(text)-2 and text[i] == first and text[i+1] == second:
                mylist.append(text[i+2])
        return mylist
print(Solution().findOcurrences("alice is a good girl she is a good student","a","good"))