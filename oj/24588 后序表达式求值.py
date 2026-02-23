import sys
data = sys.stdin.readlines()
k = int(data[0][:-1])
i = 1
for _ in range(k):
    mylist = data[i][:-1].split()
    output = []
    for s in mylist:
        if s == "+" or s == "-" or s == "/" or s == "*":
            a,b = output[-2],output[-1]
            output.pop()
            output.pop()
            if s == "+":
                output.append(a+b)
            elif s == "-":
                output.append(a-b)
            elif s == "*":
                output.append(a*b)
            elif s == "/":
                output.append(a/b)
        else:
            output.append(float(s))
    print(f"{output[0]:.2f}")
    i += 1
