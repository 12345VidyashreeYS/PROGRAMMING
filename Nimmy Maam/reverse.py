# # 1.	WAP to reverse a given number.

# n = int(input("Enter the number: "))
# rev = 0
# while n>0:
#     rem = n% 10
#     rev = (rev * 10) + rem
#     n= n//10
# print("Thr reverse is", rev)

# # 1.	WAP to reverse a given negative number.

# n= int(input("Enter the number: "))
# temp = n
# if n < 0:
#     n = n*-1
# rev = 0
# while n>0:
#     rem = n% 10
#     rev = (rev * 10) + rem
#     n= n//10
# if temp<0:
#     rev = rev*-1
# print(rev)

# using def

def reverseNum(n):
    temp = n
    if n < 0:
        n = n*-1
    rev = 0

    while n>0:
        rem = n% 10
        rev = (rev * 10) + rem
        n= n//10

    if temp<0:
        rev = rev*-1
    return rev

n= int(input("Enter the number: "))
result = reverseNum(n)
print(result)



