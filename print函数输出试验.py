a=5
b=9

print(90)
print(a)
print(a+b)
print(a*b)
                    # print()括号中若没有引号，则只能输出数字或者被赋予数字的变量
                    # 若想输出字母或字符串要加单引号''
print('liupenp')
print("liupeng")
print("""liupeng""") # 不同print函数输出，自动换行
print('''liupeng''') # 两边的引号个数相同，则不输出引号

print(a,b,'要么出众，要么出局') # 使用print函数在同一行输出
                            # 注意 中间的“,”不会输出

# 输出ASCII对应表中的字符
print('b') # 直接输出字符b
print('[')
print(chr(98)) #输出ASCII表中98对应的字符
print(chr(91))


print(ord('北'))
print(ord('京')) #输出中文的Unicode码
print(chr(21271),chr(20140)) # 输出Unicode码对应的中文汉字

# print（）输出后不换行的格式
print('北京',end='')
print('欢迎您')


