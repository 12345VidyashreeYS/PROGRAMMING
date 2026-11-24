# Write a logic to display numbers upto “n” (included) in incrementing format.

# n = int(input("Enter the number: "))
# i=2
# while i<=n:
#     print(i, end=" ")
#     i=i+1

# WAL to display natural number in decrementing order upto 1(included) in incrementing difference.
# n=11
# diff=1
# while n>0:
#     print(n, end=" ")
#     n=n-diff
#     diff=diff+1

# n= int(input("Enter the n value: "))
# diff = 1
# while n>0:
#     print(n, end=" ")
#     n=n-diff
#     diff=diff+1

# WAL to get the input number from the user until the user until the user is not entering 0. Once the user enters 0 then exit asking for the number.

# while True:  #Unlimiited loop
#     n=int(input("Enter the number: "))
#     if n== 0:
#         break
#     print("The enetered number is: ", n)
# print("The programm terminated")

# WAL to get the input number from the user until the user is not entering 0. Once the user enters 0 then exit asking for the number and also skip executing the logic whenever the user enters 5 or 7.

while True:
    n= int(input("Enter the number: "))
    if n == 0:
        break
    elif n==5 or n==7:
        continue
    print("The entered number is: ", n)
print("The program is terminated.")



    