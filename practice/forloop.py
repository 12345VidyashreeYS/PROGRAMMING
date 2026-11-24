#for with rang()

# WAL to display from 1 to 10(n) with difference of 3

n = int(input("Enter the number: "))
for i in range(1, (n+1), +3):
    print(i, end=" ")
print("\nLast i:",i)

# WAL to display n(10) to 6 with a difference of 2

# n = int(input("Enter the number: "))
# for i in range(n, (5-1), -2):
#     print(i, end=" ")
# print("\nLast i:", i)

# # fro without range():

# l1= [1, 34, "s", "djw", "Rayaru", "Sai"]
# for i in l1:
#     print(i, end=" ")

# name = "apple"
# for i in name:
#     print(i)
# print(i)

# for i in ():
#     print(i)

# for i in "4963":
#     print(i, end=" ")

# while loop

# i. Write a logic to display numbers upto “n” (included) in incrementing format.

# n = int(input("Enter the number: "))
# i= 1
# while i<=n:
#     print(i, end=" ")
#     i+=1

# ii. WAL to display natural number in decrementing order upto 1(included) in incrementing difference.

# n = int(input("Enter the number: "))
# diff = 1
# while n>=1:
#     print(n, end=" ")
#     n = n-diff
#     diff = diff+1

# iii. WAL to get the input number from the user until the user is not entering 0. Once the user enters 0 then exit asking for the number.

# while True:
#     n= int(input("Enter the number: "))
#     if n==0:
#         break
#     print("The entered number is: ", n)
# print("The program terminated!!!!")

# WAL to get the input number from the user until the user is not entering 0. Once the user enters 0 then exit asking for the number and also skip executing the logic whenever the user enters 5 or 7.

# while True:
#     n = int(input("Enter the number: "))
#     if n==0:
#         break
#     elif n==5 or n==7:
#         continue
#     print("The entered number is: ", n)
# print("The program terminated!!!!")

