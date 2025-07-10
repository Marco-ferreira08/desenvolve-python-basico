import random
nums = list()
x = random.randint(5, 20)
for i in range(x):
    nums.append(random.randint(1, 10))

print("Lista:")
print(nums)
print(f"Soma dos itens da lista: {sum(nums)}")
print(f"Média dos números da lista: {sum(nums)/len(nums)}")
