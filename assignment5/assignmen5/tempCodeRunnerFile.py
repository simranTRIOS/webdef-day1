print(b_list)
adddition =[]
multiplication = []
for i in range(3):
    adddition.append([0]*3)
    multiplication.append([0]*3)
for i in range(3):
    for j in range(3):
        adddition[i][j]=a_list[i][j] + b_list[i][j]

for i in range(3):
    for j in range(3):
        for k in range(3):
            multiplication[i][j] = multiplication[i][j] + a_list[i][k] * b_list[k][j]
print("addition matrix : ")
for i in range(3):
    for j in range(3):
        print(adddition[i][j],end=" ")
    print(' ')

print("multiplication martix: ")
for i in range(3):
    for j in range(3):
        print(multiplication[i][j],end=" ")
    print('')