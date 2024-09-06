from math import pow
x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))

z = (pow(x,2) + pow(y,2)) / (pow((x - y),2))
print (z)