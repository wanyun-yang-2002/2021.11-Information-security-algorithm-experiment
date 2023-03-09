import random
import os

# Plaintext 明文 Ciphertext 密文

Plaintext = list(input("输入明文："))
lens = len(Plaintext)

def encode():
    key = []                                            # 新建空置换列表
    for i in range(1, lens + 1):
        key.append(i)
    random.shuffle(key)                                 # 生成随机置换表
    Ciphertext = []                                     # 新建空密文列表
    for i in key:                                       # 根据置换表生成密文
        a = Plaintext[i - 1]
        Ciphertext.append(a)
    Ciphertext = ''.join(Ciphertext)
    print("密文为：", Ciphertext)
    for i in range(0, lens):                            # 数字列表变成字符列表
        key[i] = str(key[i])
    key = str(list(key))
    # 将置换列表写入文件
    f = open("数据置乱.txt", mode='w')
    f.writelines(key)
    f.close()


if not os.path.exists("数据置乱.txt"):                        # 判断替换表是否存在，若不存在则生成置乱表
    encode()
else:                                                       # 若置乱表存在
    file = open("数据置乱.txt", mode='r')                     # 读取文件
    key = list(file.readline())                             # 密钥（字符串列表）
    file.close()
    if len(key) != lens:                                    # 判断密钥长度
        encode()
    else:
        Ciphertext = []                                     # 新建空密文列表
        for i in range(0, lens):                            # 变为数字列表
            key[i] = int(key[i])
        for i in key:                                       # 根据置换表生成密文
            a = Plaintext[i-1]
            Ciphertext.append(a)
        Ciphertext = ''.join(Ciphertext)
        print("密文为：", Ciphertext)

# 解密
Ciphertext = input("输入要解密的密文：")

file = open("数据置乱.txt", mode='r')                     # 从文件中读取置换表
key = file.readline()                                   # 密钥（字符串列表）
file.close()

for i in range(0, len(key)):
    key = key.replace("'", '')
    key = key.replace('[', '')
    key = key.replace(']', ',')
    key = key.replace(' ', '')

keys = []
temp = []
cnt = 0
for i in range(0, len(key)):
    if key[i] != ',':
        cnt += 1
        temp.append(key[i])
    else:
        cnt = 0
    if cnt == 0:
        keys.append(''.join(temp))
        temp = []

for i in range(0, lens):                                # 变为数字列表
    keys[i] = int(keys[i])
ans = dict(zip(keys, Ciphertext))                       # 创建字典，密钥和密文一一对应
ans = sorted(ans.items(), key=lambda item:item[0])      # 将字典按照键的大小排序
print("解密结果为： ", end='')
for x in range(0, lens):
    print(ans[x][1], end='')
