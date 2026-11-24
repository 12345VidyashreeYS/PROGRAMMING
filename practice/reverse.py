# 1. WAP to reverse a given number.

# n= int(input("Enter the reverse number: "))
# rev = 0
# while n>0:
#     rem = n%10
#     rev = (rev*10)+rem
#     n = n//10
# print(rev, end=" ")

# 2. WAP to reverse a given negative number.

# n = int(input("Enter the reverse number: "))
# temp = n
# if n<0:
#     n = n*-1
# rev = 0
# while n>0:
#     rem=n%10
#     rev=(rev*10)+rem
#     n=n//10
# if temp<0:
#     rev=rev*-1
# print(rev)

# 3. WAP to reverse a given number using Customised function
# def revNum(n):
#     temp = n
#     if n<0:
#         n = n*-1
#     rev = 0
#     while n>0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     if temp<0:
#         rev=rev*-1
#     return rev

# n = int(input("Enter the reverse number: "))
# result = revNum(n)
# print(result)

# 4. WAP to reverse each number present in a user defined range.

def revNum(n):
    temp = n
    if n<0:
        n = n*-1
    rev = 0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if temp<0:
        rev=rev*-1
    return rev

st = int(input("starting: "))
en = int(input("ending: "))
if st > en:
    print("Invalid input")
else:
    print("The reversed numbers are: ")
    for i in range(st, en+1):
        print(revNum(i), end=" ")

    





