n=int(input("enter the number:\n"))
for i in range(1,n+1):
    for j in range(i,i+n):
        print(j,end=" ")
    print()
