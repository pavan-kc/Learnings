n = 5
for i in range(1,n+1):
    k=1
    for j in range(1,n+1):
        if i+j>=n+1:
            print(k,end=' ')
            k+=1
        else:
            print(' ',end=' ')
    print()
