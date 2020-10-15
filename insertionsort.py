a=[1,3,2,4,8,7] //also you can take input from user
for i in range(len(a)):
    key=a[i]
    j=i-1
    while key < a[j] and j>=0:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)
