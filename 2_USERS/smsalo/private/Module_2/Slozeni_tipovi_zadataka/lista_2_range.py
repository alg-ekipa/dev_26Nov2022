for i in range (1,11,2):   #range(start, stop-1, step)
    print(i, end=" ")

print("\n")

for i in range(1,11):
    print(i, end=" ")

print()

for i in range (100,-1,-5): #range(start, stop+1, step)
    print(i, end=" ")
print()

#Zbroj brojeva od 1 do 20
zbroj=0
for i in range (21):
    #print (i, end=" ")
    zbroj=zbroj+i
    #print(zbroj, end=" ")
print(f"završni zbroj je {zbroj}.")

