# x是明文 y是密文 k是密钥

# 加密函数
def f1(x, k):
    word = list(map(ord,x))         #使用list()和map()和ord()把x转换为ASCII码形式的列表
    lens = len(word)
    k = int(k)
    for i in range(lens):
        temp = word[i]
        if 65 <= temp <= 90:        #大写字母
            temp += k
            while temp > 90:
                temp -= 26
        elif 97 <= temp <= 122:     #小写字母
            temp += k
            while temp > 122:
                temp -= 26
        word[i] = temp
    word = list(map(chr, word))     #转为字母形式的列表
    word = ''.join(word)
    return word

# 解密函数
def f2(x, k):
    word = list(map(ord, x))
    lens = len(word)
    k = int(k)
    for i in range(lens):
        temp = word[i]
        if 65 <= temp <= 90:
            temp -= k
            while temp < 65:
                temp += 26
        elif 97 <= temp <= 122:
            temp -= k
            while temp < 97:
                temp += 26
        word[i] = temp
    word = list(map(chr, word))
    word = ''.join(word)
    return word


words = input("加密(1)还是解密(0)？")
msg = input("输入信息：")
if not msg.isalpha():
    print("错误！请重新输入信息：", end='')
    msg = input()

k = input("输入密钥：")
if not k.isdigit():
    print("错误！请重新输入密钥：", end='')
    k = input()

if words == "1":
    ans = f1(msg, k)
else:
    ans = f2(msg, k)
print("加密/解密结果为:", ans)
