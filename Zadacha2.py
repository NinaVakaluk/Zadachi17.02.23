# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

a= int(input("Введите трехзначное число:"))
s=0
while(a!=0):
    n=a%10
    s=s+n
    a=a//10
print(int(s))