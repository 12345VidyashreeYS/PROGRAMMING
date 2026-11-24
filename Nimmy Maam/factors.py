# def disFactors(n):
#     for i in range(1, n+1):
#         if n%i==0:
#             print(i, end=" ")
# n= int(input("Enter the factor number: "))
# disFactors(n)

# 1. WAP to display the count of factors of a given number

# def countFact(n):
#     countFactors=0
#     for i in range(1, (n+1)):
#         if n%i==0:
#             countFactors+=1
#     return countFactors

# n= int(input("Enter the factor number: "))
# res= countFact(n)
# print(res)

#Prime numbers:

# def isPrime(n):
#     count= 0
#     for i in range(1, (n+1)):
#         if n%i==0:
#             count+=1
#     return count==2

# n= int(input("Enter the number: "))
# if isPrime(n):
#     print(n, "is a Prime number")
# else:
#     print(n, "is not a prime number")

# def countCycles(n):
#     countofCycles= 0
#     for i in range(1, (n+1)):
#         if n%i==0:
#             continue
#         countofCycles+=1
#     return countofCycles

def displayFactors(n):
    print("The factors of", n, "is: ")
    for i in range(1, n+1):
        if n%i==0:
            print(i, end=" ")

def countFact(n):
    countFactors=0
    countofCycles=0
    for i in range(1, (n+1)):
        countofCycles+=1
        if n%i==0:
            countFactors+=1
    return countFactors, countofCycles

n=int(input("Enter the number: "))
displayFactors(n)
resFact, resCycles= countFact(n)
print("\nThe count of Factors of", n, "are: ", resFact)
print("The count of Cycles for", n, "are: ", resCycles)

