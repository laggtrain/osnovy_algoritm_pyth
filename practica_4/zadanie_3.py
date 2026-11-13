x = int(input("четырехзначное число - "))
thousands = x // 1000
hundreds = (x - thousands * 1000) // 100
tens = (x - thousands * 1000 - hundreds * 100) // 10
units = x - thousands * 1000 - hundreds * 100 - tens * 10

print(f"Цифра в позиции тысяч равна {thousands}")
print(f"Цифра в позиции сотен равна {hundreds}")
print(f"Цифра в позиции сотен равна {tens}")
print(f"Цифра в позиции единиц равна {units}")