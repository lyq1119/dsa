import sys

def solve():
    # 读取所有输入并转为迭代器，方便处理
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    m = int(next(it))  # 测试组数
    
    for _ in range(m):
        n = int(next(it))  # 操作步数
        
        queue = []
        stack = []
        q_error = False
        s_error = False
        
        for _ in range(n):
            op = next(it)
            if op == "push":
                k = next(it)
                # 只要没报错，就继续加
                if not q_error: queue.append(k)
                if not s_error: stack.append(k)
            else:
                # 处理队列出队
                if not q_error:
                    if not queue:
                        q_error = True
                    else:
                        queue.pop(0) # 弹出最左边
                
                # 处理栈出栈
                if not s_error:
                    if not stack:
                        s_error = True
                    else:
                        stack.pop() # 弹出最右边
        
        # 输出结果
        if q_error:
            print("error")
        else:
            print(" ".join(queue))
            
        if s_error:
            print("error")
        else:
            print(" ".join(stack))

if __name__ == "__main__":
    solve()