# 输入任意长的可见字符，将该字符串的数据转为字符型的二进制01和十六进制0-f的字符串在终端显示。
# 输入：abcdef
# 在屏幕输出二进制：01100001	01100010	01100011	01100100	01100101	01100110
# 		十六进制：61 62 63 64 65 66
# 先把字符串转为十进制ASCII码，然后再转换成二进制和十六进制

msg = list(input("输入字符串："))
l = len(msg)
for i in range(0, l):  # 字符串转为十进制数字
    msg[i] = ord(msg[i])


def Change2(lx):  # 转为二进制并输出
    print("二进制：", end='')
    for i in range(0, l):
        t = lx[i]
        t = bin(t)
        t = t.replace("0b", "0")
        print(t, end=' ')


def Change_16(lx):  # 转为十六进制并输出
    print("十六进制：", end='')
    for i in range(0, l):
        t = lx[i]
        t = hex(t)
        t = t.replace("0x", "")
        print(t, end=' ')


Change2(msg)  # 调用函数
print('\n')
Change_16(msg)
