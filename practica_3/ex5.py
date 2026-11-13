shopping_list = ["яйца","молоко","помидоры","огурцы"]
shopping_list.append("яйца")
print(shopping_list)
unique_items = set(shopping_list)
print(unique_items) # unique_items будет отличатся от shopping_list тем что:
                    # его объекты всегда будут в разном порядке, потому что множество это неупорядоченный тип данных
                    # он будет содержать только уникальные объекты без повторений