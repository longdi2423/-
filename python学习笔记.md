#                **python学习笔记**

# 一.前言

## 程序设计语言的分类

1.三种形式的语言

![屏幕截图 2025-07-07 173819](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20173819.png)

2.编译与解释

![屏幕截图 2025-07-07 174339](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20174339.png)

![屏幕截图 2025-07-07 174427](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20174427.png)

编译型的优点：源代码编译生成的目标代码可直接执行，运行速度更快。缺点：若要修改代码，只可去修改源代码，而后再重新编译，生成新的源代码。(使用makefile的项目书写方式可缩小缺点)。   

而解释型不需要编译，需要<u>**一直保留源代码**</u>，程序就可运行，修改也直接在源代码上修改就行了。

采用编译方式执行的语言就是**静态语言**  如：C/C++，java

采用解释方式执行的语言就是**脚本语言**  如：python，

## Python语言的简介与开发工具

### 历史 特点 应用

![屏幕截图 2025-07-07 181344](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20181344.png)

![屏幕截图 2025-07-07 181328](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20181328.png)

![屏幕截图 2025-07-07 181317](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20181317.png)

python解释器--IDLE

![屏幕截图 2025-07-07 183843](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20183843.png)

### 第三方开发工具PyCharm

![屏幕截图 2025-07-07 183208](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20183208.png)

# 二.基础语法

## 1.基本输出函数print

![屏幕截图 2025-07-07 210626](https://liupeng2423.oss-cn-beijing.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-07-07%20210626.png)



最简单的使用方面，就是把内容在运行终端输出。

使用方法及注意事项，见下列代码

``

```python
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

```

可以观察到print（）函数完整语法表达式中有end=\n,在这个就是造成print（）函数之后自动换行的原因，而要使输出之后不换行，则可以使用下面的代码格式

```python
# print（）输出后不换行的格式
print('北京',end='')
print('欢迎您')
```

使end后面为空，即将\n剔除

#### 使用print函数将内容输出到文件

```python
fp=open('note.txt','w') # 打开文件 w-->write
print('北京欢迎您',file=fp) # 将“北京欢迎您”输出（写入）到fp指向的文件中
fp.close() # 关闭文件
```
