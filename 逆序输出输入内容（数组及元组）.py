old = input("请输入原始字符：")
new1 = []
print("原始字符为：", old)
Olen = len(old)

'简单元组+循环转换'
for i in range(0,Olen,1):
    new1 += old[Olen -i -1]
print("简单元组+循环转换后字符：", new1)


'简单元组循环打印'
new2 = []
for i in old:
    new2.append(i)
new2.reverse()
print("简单元组+循环转换后字符：", new2)
