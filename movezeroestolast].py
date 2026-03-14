arr=[1,0,3,2,0,6,2,4,0,78,99]
n=11
empty_list=[]
non_empty_list=[]
for i in range(n):
    if arr[i]==0:
        empty_list.append(arr[i])
    else:
        non_empty_list.append(arr[i])
result=non_empty_list+empty_list
for nums in result:
    print(nums,end=" ")