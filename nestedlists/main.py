l1=[[1,2,3,4],[ 5, 6, 7, 8],[ 9, 10, 11, 12],[ 13, 14, 15, 16]]
for i in range(len(l1)):
    for j in range(len(l1)):
        print(l1[i][j],end=' ')
    print( )

l2=[[1,2,3,4],[ 5, 6, 7, 8],[ 9, 10, 11, 12],[ 13, 14, 15, 16]]
for i in range(len(l2)):
    for j in range(len(l2)):
        print(l2[i][j],end=' ')
    print( )
l3=[[],[],[],[]]
for i in range(len(l3)):
    for j in range(len(l3)):
        l3[i].append(l1[i][j]+l2[i][j])
        print(l3[i][j],end=' ')
    print( )
    




        
        


     


     