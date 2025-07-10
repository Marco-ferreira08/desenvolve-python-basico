import random

numbers = list()

for i in range(20):
    numbers.append(random.randint(-100, 100))

max_index = numbers.index(max(numbers)) 
min_index = numbers.index(min(numbers))

print("Lista em ordem crescente:")
print(sorted(numbers))
print("")
print("Lista Original")
print(numbers)
print("")
print("Índice do maior número:")
print(max_index)
print("")
print("Índice do menor número:")
print(min_index)
