<<<<<<< HEAD
def sumofdigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumofdigits(n // 10)

n = int(input("enter a number"))
=======
def sumofdigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumofdigits(n // 10)

n = int(input("enter a number"))
>>>>>>> 6bff3f60cc967a09480ce1bafc968610e1e65067
print(sumofdigits(n))