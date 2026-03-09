num=int(input())
str_num=str(num)
power=len(str_num)
total=0
for digit in str_num:
    total+=int(digit)**power
if total==num:
    print("Amstrong Number")
else:
    print("Not an Amstrong Number")