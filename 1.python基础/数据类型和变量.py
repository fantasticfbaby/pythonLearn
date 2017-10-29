# 转义部分和其他语言一样

# r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

# 用'''...'''的格式表示多行内容,r的规则默认
print('''line1\\\\
line2
line3''')
print(r'''line1\\\\
line2
line3''')

# 布尔值
print(True)
print(False)
print(3 > 2)
print(3 > 5)
print('')
# 没有！&&|| 只有not and or
print(True and False)
print(True or False)
print(not True)
print('')

# 空值None 等同于 null
print(None)

# python的变量同JavaScript一样是动态的，就是说不需要定义类型

# 两种除法， 一种是普通除，一种是地板除
print(10/3)
print(9/3)
print(10//3)  # 只取结果的整数部分
print(9//3)
