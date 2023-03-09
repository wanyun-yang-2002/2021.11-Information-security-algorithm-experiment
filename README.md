# 2021.11-Information-security-algorithm-experiment
# 西安邮电大学信息安全算法实验/实习 - 大二上 - 2021.11

### 一、实验目的和要求
- 实验目的：建立系统设计的整体思想，锻炼编写程序、调试程序的能力，学习文档编写规范，培养独立学习、吸取他人经验、探索前言知识的习惯，树立团队协作精神。
- 实验要求：使用Python、C、Java等语言根据题目要求编写程序。

### 二、实验原理
<br>1. 移位加密<br>
输入一串字母组成的字符s，再输入一个密钥k，将明文字符串中的每个字符向后移动k位进行加密，将密文字符串中每个字符向前移动k位进行解密。<br>
举例：加密（密钥为3）：abc -> def<br>
&emsp;&emsp;&ensp;&nbsp;&nbsp;解密（密钥为3）：abc -> xyz
<br>2. 替换加密<br>
输入一串由字母、数字组成的字符s，通过随机生成的一张替换表（由26个英文字母和数字组成）进行加密解密。<br>
举例：<br>若替换表为：abcdefghijklmnopqrstuvwxyz0123456789<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;h2ugim7vfaqw0ctpr9j3bdlyox81se456nzk
     <br>&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; 则明文abcd对应的密文为h2ug
<br>3. 数据置乱<br>
输入由可见字符组成的字符串，根据字符个数生成随机置乱表，通过置换表进行加密解密。<br>
举例：若明文为：abc123[]\啊喔呃<br>
      &emsp;&emsp;&ensp;&nbsp;&nbsp;根据字符数生成的置乱表为：9, 4, 8, 1, 3, 2, 12, 10, 6, 5, 7, 11<br>
      &emsp;&emsp;&ensp;&nbsp;&nbsp;则对应的密文为：\1]acb呃啊32[喔<br>
&emsp;&emsp;&ensp;&nbsp;&nbsp;其中第9位的\移动到了第1位，第4位的1移动到了第二位......以此类推。
<br>4. 分组加密<br>
将明文根据密钥中字符数进行分组，然后通过依次移位进行加密。
若密钥为k位，则将明文每k位分为一组，然后每一组的明文依次向后移动1位、2位、3位......k位<br>
举例：明文：abcdefghi  &emsp;密钥：abc<br>
&emsp;&emsp;&ensp;&nbsp;&nbsp;将明文每三个字符（密钥abc由3个字符组成）分为一组，然后每一组依次移一位、两位、三位进行加密：a -> b（移1位），b -> d（移2位），c -> f（移3位），d -> e（移1位），e -> g（移2位），f -> i（移3位），g -> h（移1位），h -> j（移2位），i ->l（移3位）。<br>
最终得到的密文为：edfbgihjl
<br>5. 字符串转二进制和十六进制<br>
先将字符串中的字符分别转为十进制的ASCII码，然后再将十进制的ASCII码转化为二进制、十六进制。<br>
举例：字母a：转为十进制ASCII码为97，97再转为二进制为01100001，97转为十六进制为61。
<br>6. 流式加密<br>
先将明文字符转为对应的十进制ASCII码，然后将其转为对应的二进制明文。随机生成等长的二进制密钥，二进制明文和二进制密钥通过按位异或进行加密，最终得到密文。<br>
举例：明文：ab  ->  二进制明文：&nbsp;01100001 01100010<br>
&emsp;&emsp;&ensp;&nbsp;&nbsp;随机生成等长二进制密钥：01100110 00100100<br>
&emsp;&emsp;&ensp;&nbsp;&nbsp;通过按位异或得到密文：&emsp;00000111 01000110
