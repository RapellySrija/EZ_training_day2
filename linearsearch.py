#linear search
def linear(li,target):
    for i in li:
        if i==target:
            print(i)
            return True
    return False
n=int(input())
li=list(map(int,input().strip().split()))[:n]
print(li)
target=int(input())
print(linear(li,target))
