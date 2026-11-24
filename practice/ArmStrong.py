def countDig(n):
    count=0
    while n>0:
        n = n//10
        count +=1
    return count

def Asn(n):
    temp = n
    pow = countDig(n)
    asn = 0
    while n>0:
        base= n%10
        asn = asn +(base ** pow)
        n = n//10
    return temp == asn

n = int(input("Enter the number: "))
if Asn(n):
    print(n, "is an Arm-Strong Number")
else:
    print(n, "is not an Arm-Strong Number")
    