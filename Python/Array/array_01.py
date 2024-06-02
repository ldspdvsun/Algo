import random

# 初始化数组
arr: list[int] = [0]*10

# 赋值
for i in range(0,len(arr)):
    arr[i]=random.randint(0,10*len(arr))

# 访问元素
for i in range(0,len(arr)):
    print(arr[i])

print(f"*"*20)

def arrays_init(arrays:list[int])  -> list:
    """初始化数组"""
    for i in range(0,len(arrays)-1):
        arrays[i]=random.randint(i,i*10*len(arrays))
    return arrays

def arrays_print(arrays:list[int]) -> int:
    """打印数组"""
    for i in range(0,len(arrays)-1):
        print(arrays[i],end=" ")
    print("")

def arrays_random_access(arrays:list[int]) -> int:
    """随机访问元素"""
    # 在区间[0,len(arrays)-1]中随机抽取一个数字
    random_index = random.randint(0,len(arrays)-1)
    # 获取随机返回元素
    random_num = arrays[random_index]
    return random_num


def arrays_insert(arrays:list[int],value:int,index:int):
    """插入元素 在arrays数组index的位置插入value"""
    for i in range(len(arrays)-1,index,-1):
        arrays[i]=arrays[i-1]
    arrays[index]=value

arrs = arrays_init(arr)
arrays_print(arrs)
arrays_insert(arrs,222,4)
arrays_print(arrs)
print(arrays_random_access(arrs))