minutes_input = int(input("минуты - "))
hours = minutes_input // 60
minutes = minutes_input-hours * 60
print(f"{minutes_input} минут - это {hours} часов {minutes} минут")