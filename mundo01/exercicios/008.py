#DESAFIO 08
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input("Metros: "))
km = valor / 1000
hm = valor / 100
dan = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print(f"Kilômetros = {km:.1f} \nHectômetro = {hm:.1f} \nDecâmetro = {dan:.1f} \nMetros = {valor:.0f} \nDecímetro = {dm:.0f}dm \nCentímetro = {cm:.0f}cm \nMilímetro = {mm:.0f}mm")
