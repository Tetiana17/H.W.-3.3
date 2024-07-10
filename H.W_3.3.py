my_list = [1, 2, 3]
# знаходимо сердній елемент
half = len(my_list) // 2
# перевіряємо на  парність та прописуємо умову
if len(my_list) % 2 == 0:
    result = my_list[:half], my_list[half:]
else:
    result = (my_list[:half + 1]), (my_list[half:] * 0 + my_list[half + 1:])
print(result)



