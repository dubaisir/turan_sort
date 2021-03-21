import random
import sys
import time


def turan_sort(lis):
    a = time.time()
    l_t = {}
    l_o = []
    cur = -1
    for i in lis:
        # 构造有序字典
        if i not in l_t.keys():
            for key_i in range(cur + 1, i + 1):
                l_t[key_i] = []
            cur = i
        # 遍历目标列表，构造顺序结构
        l_t[i].append(1)
    # 遍历顺序结构，打印结果
    for key in l_t.keys():
        if l_t[key]:
            for i in l_t[key]:
                l_o.append(key)

    print(l_o)
    b = time.time()
    print(sys._getframe().f_code.co_name + '用时：' + str((b - a) * 1000) + 'ms')


data = []
for i in range(100):
    data.append(int(random.random() * 1000))
print(data)
turan_sort(data)
