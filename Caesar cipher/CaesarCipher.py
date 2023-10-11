#Prime number checker
num = int(input())
def prime(num):

    if num == 1:
        num = "it's not a prime number"
        return num

    elif num == 2:
        num = "its a prime number"
        return num

    elif not(num % 2 == 0):
        num = "it's a prime number"
        return num

    else:
        num = "it's not a prime number"
        return num

    

print(prime(num))
