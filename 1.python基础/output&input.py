# 可以用逗号隔开接受多个字符串
print('The quick brown fox', 'jumps over', 'the lazy dog')

# 打印整数
print(300)
print(100+200)
print('100+200', 100+200)

# 输入
name = input()
print(name)

# 有提示的输入
name = input('please enter your name: ')
print('your name is :', name)

n=123
f=456.789
s1=("'Hello,world'")
s2=(r"'Hello,\'Adam\'''")
s3=('r\'Hello,"Bart"\'')
s4=("r'''Hello,\nLisa!'''")
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
# 设置sep='\n'
print(n,f,s1,s2,s3,s4,sep='\n')

with open('tmp.txt','w') as tmp:
    print('Hello', 'World', end='End', sep='-', file=tmp)
