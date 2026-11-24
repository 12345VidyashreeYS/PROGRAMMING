n=int(input("Enter the number:"))
i=3
while i<n:
    print(i,end=" ")
    i+=1
print("\nLast i:", i)


n=int(input("Enter a number:"))
diff=1
while n>=0:
    print(n, end=" ")
    n=n-diff
    diff=diff+1
print("\n Last n:", n)

