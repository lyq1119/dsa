import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    stack = []
    ptr = 1 
    
    results = [] 
    
    for _ in range(n):
        op = input_data[ptr]
        if op == 'push':
            k = input_data[ptr + 1]
            stack.append(k)
            ptr += 2
        else: 
            if not stack:
                results.append("-1")
            else:
                results.append(stack.pop())
            ptr += 1
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()