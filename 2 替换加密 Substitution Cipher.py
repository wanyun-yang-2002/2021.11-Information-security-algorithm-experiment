# 输入一个字母和数字组成明文字符串，并能随机产生一个替换表作为密钥保存到文件并显示出来，然后根据替换表进行数据变换加密。
# 在解密时导入文件中的替换表，根据该替换表进行解密。
# Plaintext 明文 Ciphertext 密文

import random
import os

Plaintext = list(input("输入明文："))
for i in range(0, len(Plaintext)):
    if not Plaintext[i].isalnum():
        print("错误！请重新输入信息：")
        Plaintext = input("输入明文：")
        break

l = len(Plaintext)

key_chart_1 = []                                 # 新建空字母表
for i in range(97, 123):
    key_chart_1.append(chr(i))
for i in range(48, 58):
    key_chart_1.append(chr(i))


if not os.path.exists("替换加密.txt"):                 # 判断替换表是否存在，若不存在则生成替换表
    key_chart_2 = []                                 # 新建空替换表
    for i in range(97, 123):
        key_chart_2.append(chr(i))
    for i in range(48, 58):
        key_chart_2.append(chr(i))
    random.shuffle(key_chart_2)                     # 生成随机替换表
    chart_1 = dict(zip(key_chart_1, key_chart_2))   # 字母表和替换表组成字典
    # 加密
    Ciphertext = []                                 # 新建空密文列表
    for i in range(0, l):                           # 使用随机替换表进行加密
        for x in chart_1.keys():
            if Plaintext[i] == x:
                Ciphertext.append(chart_1[x])
    Ciphertext = ''.join(Ciphertext)                # 密文列表转为字符串
    print("加密结果为：", Ciphertext)
    key_chart_2 = ''.join(key_chart_2)
    f = open("替换加密.txt", mode='w')                # 新建txt文件
    f.write(key_chart_2)                            # 写入替换表
    f.close()                                       # 关闭文件
else:
    file = open("替换加密.txt", mode='r')             # 打开文件
    key = list(file.readline())                     # 读取替换表
    file.close()                                    # 关闭文件
    Ciphertext = []                                 # 新建空密文列表
    chart_1 = dict(zip(key_chart_1, key))           # 字母表和替换表组成字典
    for i in range(0, l):                           # 使用随机替换表进行加密
        for x in chart_1.keys():
            if Plaintext[i] == x:
                Ciphertext.append(chart_1[x])
    Ciphertext = ''.join(Ciphertext)                # 密文列表转为字符串
    print("加密结果为：", Ciphertext)

# 解密
file = open("替换加密.txt", mode='r')             # 打开文件
key = list(file.readline())                     # 读取替换表
file.close()                                    # 关闭文件

Ciphertext = input("输入要解密的密文：")

chart_2 = dict(zip(key, key_chart_1))           # 读取到的替换表和字母表组成字典chart_2
ans = []                                        # 新建解密列表
print("解密结果为： ", end='')
for i in range(0, l):                           # 解密
    for x in chart_2.keys():
        if Ciphertext[i] == x:
            ans.append(chart_2[x])
ans = ''.join(ans)                              # 解密结果转为字符串形式
print(ans)
