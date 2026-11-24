# n= int(input("Enter the number: "))
# count=0
# while n>0:
#     n=n//10
#     count=count+1
# print(count)

# def countDigits(num):
#     count = 0
#     while num>0:
#         num = num// 10
#         count = count+1
#     return count

# n= int(input("Enter the number: "))
# res=countDigits(n)
# print(res)

def countDigits(num):
    count = 0
    while num>0:
        num = num// 10
        count = count+1
    return count

def isASN(n):
    temp=n

    if n<0:
        n= n*-1

    pow=countDigits(n)
    asn=0
    while n>0:
        base= n%10
        asn=asn+(base**pow)
        n=n//10

    if temp<0:
        asn = asn*-1
        
    return temp==asn

# n=int(input("Enter the number: "))
# if isASN(n):
#     print(n, "is an ASN")
# else:
#     print(n, "is not an ASN")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
if start > end:
    print("Invalid Input")
else:
    for i in range(start, end+1):
        if isASN(i):
            print(i, "is an ARM number")
        else:
            print(i, "is not ARM number")

# else:
#     for i in range(start, end+1):
#         print(isASN(i), end=" ")


