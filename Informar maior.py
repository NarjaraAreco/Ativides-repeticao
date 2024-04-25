# Faça um programa que leia 10 números e informe o maior número.
y=0
for i in range (1, 11):  
    x = int(input())
    if x > y:   
        y = x
print(y)