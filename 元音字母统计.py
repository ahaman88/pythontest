word = input("请输入字符串：")
print("刚才输入的字符串为：",word)
word1 = word.upper()


print("字符串总长度为：",len(word1), "个")

a = 0
e = 0
i = 0
o = 0
u = 0

type(word1)

"元音字母A"
for z in range(0, len(word1), 1):
    if word1[z] == "A":
        a += 1
        print (nl[0])
        nl[0] += 1

print ("元音字母A共有： %d 个，占总字符串数比例为：%.2f %%" %(a, a / len(word) * 100))


"元音字母E"
for z in range(0, len(word1), 1):
    if word1[z] == "E":
        e += 1

print ("元音字母E共有： %d 个，占总字符串数比例为：%.2f %%" %(e, e / len(word) * 100))


"元音字母I"
for z in range(0, len(word1), 1):
    if word1[z] == "I":
        i += 1

print ("元音字母I共有： %d 个，占总字符串数比例为：%.2f %%" %(i, i / len(word) * 100))

"元音字母O"
for z in range(0, len(word1), 1):
    if word1[z] == "O":
        o += 1

print ("元音字母O共有： %d 个，占总字符串数比例为：%.2f %%" %(o, o / len(word) * 100))

"元音字母U"
for z in range(0, len(word1), 1):
    if word1[z] == "U":
        u += 1

print ("元音字母U共有： %d 个，占总字符串数比例为：%.2f %%" %(u, u / len(word) * 100))

