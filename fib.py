def fib(n):
    standard_values=[0,1]
    for i in range(2,n):
        new=standard_values[-1]+standard_values[-2]
        standard_values.append(new)
    return standard_values
n=int(input("enter a number"))
print(fib(n))