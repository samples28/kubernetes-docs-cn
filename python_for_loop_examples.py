# Python for 循环示例

# 1. 基本的数字循环
print("1. 基本数字循环:")
for i in range(5):
    print(f"数字: {i}")

print("\n" + "="*40 + "\n")

# 2. 指定范围的循环
print("2. 指定范围循环 (2到8):")
for i in range(2, 9):
    print(f"数字: {i}")

print("\n" + "="*40 + "\n")

# 3. 指定步长的循环
print("3. 指定步长循环 (0到10，步长为2):")
for i in range(0, 11, 2):
    print(f"偶数: {i}")

print("\n" + "="*40 + "\n")

# 4. 遍历列表
print("4. 遍历列表:")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
for fruit in fruits:
    print(f"水果: {fruit}")

print("\n" + "="*40 + "\n")

# 5. 使用enumerate获取索引和值
print("5. 使用enumerate获取索引和值:")
colors = ["红色", "蓝色", "绿色", "黄色"]
for index, color in enumerate(colors):
    print(f"索引 {index}: {color}")

print("\n" + "="*40 + "\n")

# 6. 遍历字典
print("6. 遍历字典:")
student_grades = {"张三": 85, "李四": 92, "王五": 78, "赵六": 96}

# 遍历键
print("遍历键:")
for name in student_grades:
    print(f"学生: {name}")

print("\n遍历键值对:")
for name, grade in student_grades.items():
    print(f"{name}的成绩: {grade}")

print("\n" + "="*40 + "\n")

# 7. 遍历字符串
print("7. 遍历字符串:")
text = "Python"
for char in text:
    print(f"字符: {char}")

print("\n" + "="*40 + "\n")

# 8. 嵌套循环
print("8. 嵌套循环 - 九九乘法表:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i * j:2d}", end="  ")
    print()  # 换行

print("\n" + "="*40 + "\n")

# 9. 列表推导式 (简化的for循环)
print("9. 列表推导式:")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"原列表: {numbers}")
print(f"平方列表: {squares}")

# 带条件的列表推导式
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

print("\n" + "="*40 + "\n")

# 10. 使用zip同时遍历多个列表
print("10. 使用zip同时遍历多个列表:")
names = ["小明", "小红", "小刚"]
ages = [20, 22, 21]
cities = ["北京", "上海", "广州"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}岁, 来自{city}")

print("\n" + "="*40 + "\n")

# 11. break和continue的使用
print("11. break和continue的使用:")
print("使用break:")
for i in range(10):
    if i == 5:
        print("遇到5，停止循环")
        break
    print(f"数字: {i}")

print("\n使用continue:")
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(f"奇数: {i}")

print("\n" + "="*40 + "\n")

# 12. else子句 (循环正常结束时执行)
print("12. for-else结构:")
for i in range(3):
    print(f"循环 {i}")
else:
    print("循环正常结束")

# 当循环被break中断时，else不会执行
print("\n带break的for-else:")
for i in range(5):
    if i == 2:
        print("提前退出循环")
        break
    print(f"循环 {i}")
else:
    print("这句不会被执行")