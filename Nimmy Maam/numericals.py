# Write a program to check whether the give number is even or odd

# num = int(input("Enter the number: "))
# if num%2 == 0:
#     print(num, "is Even")
# else:
#     print(num, "is Odd")
# print(num%2 == 0)

# Write a program to check whether the given num is even or odd using customised function.

# def isEvenOdd(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input("Enter the number: "))
# if isEvenOdd(num):
#     print(num, "is Even")
# else:
#     print(num, "is Odd")

# Code Optimization

# def isEvenOdd(n):
#     n % 2 == 0

# num = int(input("Enter the number: "))
# if isEvenOdd(num):
#     print(num, "is Even")
# else:
#     print(num, "is Odd")

# WAP to display all the even and odd numbers present in a user defined range seperately

# def isEven(n):
#     return n % 2 == 0

# num = int(input("Enter the number: "))
# for i in range(3, (8+1), 2):
#     if isEven(num):
#         print(i, end=" ")


# def isEvenOdd(n):
#     return n  % 2==0

# num=int(input("enter a num:"))
# for i in range(3, num + 1):
#     if isEvenOdd(i):
#         print(i,end=" ")
#     else:
#         print(i, "is odd")


# def isEvenOdd(n):
#     return n % 2==0

# num=int(input("enter a num:"))
# for i in range( 1 , num +1):
#     if isEvenOdd(i):
#         print(i, "is Even")
#     else:
#         print(i, "is odd")


# def isEvenOdd(n):
#     return n  % 2==0

# num=int(input("enter a num:"))
# for i in range(2, num + 1):
#     if isEvenOdd(i):
#         print(i,end=" ")

# def isEvenOdd(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input("Enter the number: "))
# if isEvenOdd(num):
#     print(num, "is Even")
# else:
#     print(num, "is Odd")

def isEvenOdd(n):
    if n%2 == 0:
        return True
    else:
        return False

num = int(input("Enter the number: "))
for i in range(3, (num+1)):
    if isEvenOdd(num):
        print(i, end=" ")
    else:
        print(i, "is odd")

# g. WAL to display first “n” even numbers.

# def isEvenOdd(n):
#     return n%2 == 0

# n = int(input("Enter tthe number: "))
# series = 1
# print("First", n, "Even numners")

# while n>0:
#     if isEvenOdd(series):
#         print(series, end=" ")
#         n-=1
#     series += 1

# WAL to display first “n” odd numbers.

# def isEvenOdd(n):
#     return n%2 == 0

# n = int(input("Enter the number: "))
# series = 1
# print("First", n, "odd numners")

# while n>0:
#     if not isEvenOdd(series):
#         print(series, end=" ")
#         n-=1
#     series +=1






