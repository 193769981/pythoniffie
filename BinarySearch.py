#A searching technique which has a time complexity of O(log n)

l = [int(x) for x in input().split()] #takes list as input
ele = int(input()) #reading the required number
lb, ub = 0, len(l) - 1 #defining the lower bound and the upper bound
mid = (lb + ub) // 2
flag = 0
# add l.sort() if input can be unsorted as this searching method is applicable only for sorted list

while(lb <= ub):
    mid = (lb + ub) // 2

    if __________:
        _________
    elif ele > l[mid]:
        lb = mid + 1
    else:
        ub = mid - 1

if _ _ _ :
    _ _ _ _ _ _ _ _ _ _ _ _ 
else:
    _ _ _ _ _ _ _ _ _ _ _ _ 
