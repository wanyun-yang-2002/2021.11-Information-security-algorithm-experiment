# 输入一个字母组成明文字符串，并输入一个字母组成的密钥，对明文进行分组后与密钥进行移位加密，输入密文以及密钥可以进行解密
# 实例：
# 输入字符串：abcdef
# 输入密钥：abc
# 输出：bdfegi
# 注意：输入的明文在分组时不足的部分要采用特殊字符进行标记进行处理。


# 分组
def Grouping(msg, k):
    group_t = []
    group = []
    cnt = 0
    for i in range(0, len(msg)):
        group_t.append(msg[i])
        if (i + 1) % len(k) == 0:
            group_t = ''.join(group_t)
            group.append(group_t)
            group_t = []
    return group


# 加密
def encode(group):
    ans = []
    l_group = len(group)
    for i in range(0, l_group):
        temp = group[i]
        for j in range(0, len(temp)):
            t = temp[j]
            t = ord(t) + j + 1
            if (t > 122) or ((t < 97) and (t > 90)):
                t -= 26
            t = chr(t)
            ans.append(t)
    ans = ''.join(ans)
    print("加密结果为：", ans)


# 解密
def decode(group):
    ans = []
    l_group = len(group)
    for i in range(0, l_group):
        temp = group[i]
        for j in range(0, len(temp)):
            t = temp[j]
            t = ord(t) - j - 1
            if (t < 65) or ((t < 97) and (t > 90)):
                t += 26
            t = chr(t)
            ans.append(t)
    ans = ''.join(ans)
    print("解密结果为：", ans)


# 调用函数

Pt = []                         # 新建明文列表
Ct = []                         # 新建密文列表

text = input("加密(1)还是解密(0)？")
text = int(text)
if text != 1 and text != 0:
    print("请重新选择：加密(1)还是解密(0)？", end='')
    text = input()
    text = int(text)
if text == 1:
    Pt = list(input("输入明文："))
    key = input("输入密钥：")
    if len(Pt) % len(key) != 0:         # 判断密钥是否合理
        print("错误！请重新输入密钥：", end='')     # 输入明文在分组不足时进行处理
        key = input()
    encode(Grouping(Pt, key))
else:
    Ct = list(input("输入密文："))
    key = input("输入密钥：")
    decode(Grouping(Ct, key))
