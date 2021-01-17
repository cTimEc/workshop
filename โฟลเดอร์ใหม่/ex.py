# จงแสดง "banana"
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# จงแก้ไขข้อมูลจาก "apple" เป็น "kiwi"
thislist = ["apple", "banana", "cherry"]
thislist[0] = "kiwi"
print(thislist)

# จงเพิ่ม "kiwi" ไปยัง fruits list
fruits = ["apple", "banana", "cherry"]
fruits.add("kiwi")
print(fruits)

# จงเพิ่ม "lemon" ไประหว่าง "apple" กับ "ิิbananna"
fruits = ["apple", "banana", "cherry"]
fruits.append("lemon"[1])
print(fruits)

# จงลบ "cherry" จาก list
fruits = ["apple", "banana", "cherry"]
fruits.remove("cherry")
print(fruits)


# จงแสดงตัวสุดท้ายของ fruits
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# จงแสดงจำนวนของ fruits
fruits = ["apple", "banana", "cherry"]
print(len(fruits))