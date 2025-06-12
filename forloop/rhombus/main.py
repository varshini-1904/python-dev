
for i in range(1,4):
    for j in range(1,8):
        if j>4-i and j<4+i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,8):
        if j>4-i and j<4+i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()