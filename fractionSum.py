def gcd(a, b):
    if (a == 0):
        return b
    return gcd (b % a, a)

def lowestValue(den3, num3):
    commonFactor = gcd(num3, den3)
    den3 = int(den3 / commonFactor)
    num3 = int(num3 / commonFactor)
    print(num3)
    print(den3)

def addFraction(num1, den1, num2, den2):
    den3 = gcd(den1, den2)
    den3 = (den1 * den2 / den3)
    num3 = ((num1) * (den3 / den1) + (num2) * (den3 / den2))
    lowestValue(den3, num3)

num1 = int(input())
den1 = int(input())
num2 = int(input())
den2 = int(input())

addFraction(num1, den1, num2, den2)