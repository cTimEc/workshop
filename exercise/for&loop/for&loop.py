# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
print("for")
c = 2
for number in range(2, 13):
    print("  [", c, "]")
    for i in range(1, 13):
        result = number * i
        print(number, "*", i, ":", result)
    print("-------------")
    c += 1