marks=[81,83,86,"Abrar",94,91,True]
print(marks)

print(marks[0])                       #indexing
print(marks[2])
print(marks[3])
print(marks[6])


print(marks[-7])                     #Negative Indexing
print(marks[-4])

print(marks[:])
print(marks[1:])
print(marks[:6])
print(marks[1:6])
print(marks[1:6:2])

if "Abrar" in marks :
    print("YES")
else:
    print("NO")


if "Abr" in "Abrar " :
    print("YES")
else : 
    print("NO")


list=[a for a in range(5)]
print(list)
list=[a*a for a in range(5)]                 
print(list)

list=[a for a in range(51) if a%2==0]
print(list)
