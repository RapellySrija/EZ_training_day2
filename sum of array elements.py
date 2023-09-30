#sum of array elements
n=int(input())
array=list(map(int,input().strip().split()))[:n]
sum=0
for i in array:
    sum = sum +i
    print(sum)
print(sum)
