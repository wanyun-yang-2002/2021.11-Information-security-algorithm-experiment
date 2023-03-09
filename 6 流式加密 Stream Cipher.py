# 输入一个任意长度可见字符串组成的字符串，并随机生成一个等长度的随机密钥并保存在文件中，采用按位异或的方式进行二进制加密，
# 并将该加密结果保存在一个文件中，解密时导入该密文和密钥进行解密，将解密结果进行输出。
# 示例：
# 输入	            a	        b	        c	        d	        e	        f
# 明文的二进制	01100001	01100010	01100011	01100100	01100101	01100110
# 二进制密钥	    01111001	01110101	01100100	01100101 	01101111	01110111
# 二进制明文     	00011000	00010111	00000111	00000001	00001010	00010001

import random
import os

msg = list(input("输入字符串："))
l = len(msg)
for i in range(0, l):  # 字符串转为十进制数字
    msg[i] = ord(msg[i])
    msg[i] = bin(msg[i])  # 转为二进制
    if len(msg[i]) > 8:
        msg[i] = msg[i].replace("0b", "0")
    else:
        msg[i] = msg[i].replace("0b", "00")


# 创建密钥
def create_keys():
    random_key = []                                     # 新建空二进制密钥列表
    for i in range(0, len(msg[0]) * len(msg)):          # 生成二进制密钥
        random_number = ''.join(random.sample(["0", "1"], 1))
        random_key.append(random_number)
    random_key = ''.join(random_key)
    # 保存密钥到文件里
    file = open("流式加密.txt", mode='w')
    file.write(random_key)
    file.close()


# 按位异或加密
def encode():
    f = open("流式加密.txt", mode='r')
    random_key = f.readline()                          # 读取文件中保存的密钥
    f.close()
    t2 = []
    for i in range(0, len(msg)):
        t1 = msg[i]
        for j in range(0, len(msg[i])):
            t2.append(str(int(t1[j]) ^ int(random_key[j + i * len(msg[i])])))
        t2 = ''.join(t2)
        msg[i] = t2
        t2 = []
    print("加密结果为：", end='')
    for i in range(0, l):
        print(msg[i], end=' ')
    print('\n')


if not os.path.exists("流式加密.txt"):
    create_keys()
    encode()
else:
    f = open("流式加密.txt", mode='r')                      # 读取文件中保存的密钥
    key = f.readline()
    f.close()
    if len(key) / len(msg) < len(msg):
        create_keys()
        encode()


# 解密
Ciphertext = input("输入要解密的密文：")
Ciphertext = list(Ciphertext.replace(" ", ''))

f = open("流式加密.txt", mode='r')                          # 读取文件中保存的密钥
key = f.readline()
f.close()

de_code = []
to_str = ''
t2 = []

for i in range(0, len(Ciphertext)):
    to_str += Ciphertext[i]
    if (i + 1) % 8 == 0:
        de_code.append(to_str)
        to_str = ''

# 按位异或解密
for i in range(0, len(de_code)):
    t1 = de_code[i]
    for j in range(0, len(de_code[i])):
        t2.append(str(int(t1[j]) ^ int(key[j + i * len(de_code[i])])))
    t2 = ''.join(t2)
    de_code[i] = t2
    t2 = []

print("解密结果为：", end='')
ans = []
for i in range(0, len(de_code)):
    de_code[i] = chr(int(de_code[i], 2))  # 字符串转十进制数字后转为字符
    ans = ''.join(de_code)
print(ans)
