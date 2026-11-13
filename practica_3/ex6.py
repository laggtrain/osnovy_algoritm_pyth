name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую):")
subjects_list = subjects_str.split(",")
age_int = int(age_str)
student = {name: (age_int, subjects_list)}

print("="*30)
print("Анкета студента")
print("="*30)

print(f"Имя: {list(student.keys())[0]}")
print(f"Возраст: {student[name][0]}")
print(f"Имя: {student[name][1]}")
print("="*30)