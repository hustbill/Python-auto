import numpy as np
l=0
for i in range(1, 10001): # 实验10000次
    a = np.random.randint(0, 2)
    b = np.random.randint(0, 2)
    c = []
    c.append(a)
    c.append(b)
    print(c)
    while (c[-1] + c[-2]) != 2:
        c.append(np.random.randint(0,2))
    l = l + len(c) # c的长度就是每次实验掷硬币的次数，加和就是10000次试验中一共掷了多少次硬币
print(l/10000) # 除以实验的次数就是每次平均需要掷多少次
