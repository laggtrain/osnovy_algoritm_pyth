from math import *

SEATS_PER_COMPARTMENT = 4

seat_number = int(input("Введите номер места - "))
coupe = ceil(seat_number / SEATS_PER_COMPARTMENT)
print(f"Ваше купе номер - {coupe}")
