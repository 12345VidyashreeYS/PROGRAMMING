# def subNum(n1, n2):
#     n=n1-n2
#     return n
# num1=20
# num2=10
# num=subNum(num1, num2)
# print(num)
# print(num+3)
# print(5+num)
# result=subNum(12, num)
# print(result)

# 1. Write a program to check whether the give number is even or odd.

# n = int(input("Enter the number: "))
# if n%2==0:
#     print("It is an even number")
# else:
#     print("It is an odd number")

# 2. Write a program to check whether the given num is even or odd using customised function.

# def EvenOdd(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# n = int(input("Enter the number: "))
# if EvenOdd(n):
#     print("It is Even")
# else:
#     print("It is an Odd")

# 3. WAP to display all the even numbers present in a user defined range.

def EvenOdd(n):
    if n%2==0:
        return True
    else:
        return False

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

if start>end:
    print("Invalid input")

else:
    print("The even numbers are: ")
    for i in range(start, end+1):
        if EvenOdd(i):
            print(i, end=" ")
    print("\nThe odd numbers are: ")
    for i in range(start, end+1):
        if not EvenOdd(i):
            print(i, end=" ")


