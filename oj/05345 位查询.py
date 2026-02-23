import sys
input = sys.stdin.read()
data = input.split()
m,n = int(data[0]),int(data[1])
mylist = [int(data[i]) for i in range(2,2+m)]
for i in range(2+m,2+m+2*n,2):
    if data[i] == "C":
        a = int(data[i+1])
        mylist = [(num+a)&65535 for num in mylist]
    else:
        a = int(data[i+1])
        a = 1<<a
        mylist1 = [a&num for num in mylist]
        print(m-mylist1.count(0))