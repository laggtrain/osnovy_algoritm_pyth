from math import *

def get_distance():
    x_1, y_1 = map(float, input("Введите x и y координаты через пробел для первой точки - ").split())
    x_2, y_2 = map(float, input("Введите x и y координаты через пробел для второй точки - ").split())
    distance =  sqrt(pow((x_1 - x_2), 2) + pow((y_1 - y_2), 2))
    print(f"{distance:.2f} см - Евклидово расстояние")

get_distance()
