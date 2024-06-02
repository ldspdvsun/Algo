for i in range(10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {i*j}", end=" ")
        if j == i:
            print("")


def for_loop(n:int) -> int:
    """for 循环"""
    res = 0
    for i in range(n+1):
        res += i
    return res

def while_loop(n:int)->int:
    """while 循环"""
    i = 0
    res = 0
    while i<= n:
        res += i
        i += 1
    return res

def recur(n:int)-> int:
    """递归"""
    # 终止条件
    if n == 1:
        return 1
    # 递: 递归调用
    res = recur(n-1)
    # 归：返回结果
    return n+res

print(for_loop(100))
print(while_loop(100))
print(recur(100))