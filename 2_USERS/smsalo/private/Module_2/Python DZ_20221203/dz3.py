a=int(input("Unesite 5-znamenkasti broj"))
a1=a//10000
a2=(a%10000)//1000
a3=(a%1000)//100
a4=(a%100)//10
a5=(a%10)
print (f"Znamenke su {a1}, {a2}, {a3}, {a4} i {a5}")