lanche = ("Humburguer","Cachorro-quente","Pastel de angu","Sorvete")
#Tuplas são IMUTÁVEIS
print(lanche)
print(lanche[1], lanche[2])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:2])
print(lanche[::-1]) #inverte a tupla, lista

print("-"*20)

for comida in lanche:
  print(f"Oto comendo um {comida}")

print("-"*20)

for count in range(0, len(lanche)):
  #print(count)
  print(f"{count+1} - {lanche[count]}")

print("-"*20)

for pos, comida in enumerate(lanche):
  print(f"{pos+1} - {comida}")

print("-"*20)

print(sorted(lanche))

print("-"*20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5)) #quantos elementos
print(c.index(8)) #posição
print(c.index(5, 1)) #deslocamento

pessoa = ("Preludio", 29, "M", 55)
print(pessoa)
#del(pessoa) apaga o elemento

