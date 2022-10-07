# Given an array of integers temperatures represents the daily temperatures
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# [72, 70, 68, 73, 74]
# [3, 2, 1, 1, 0]

'''
[-2, -2, 5]

[0, 1, 2, 3]
[68, 70, 71, 60]

[60, 70, 71, 63, 01, 02] 6
[1, 1, 0, 0, 0, 0] 2

[70, 68, 50, 30, 10, 71]

r = 5
l = 0

71-70 

i : [0, 1, 2, 3, 4]
r-l+i = r-l = 5
r-(l+i) = r-(l+1) = 4

[0, 1, 2, 3, 4, 5]

d = [2, 2, 1, 0]
[1, 1, 0, 0]

'''

def days_until_hottest(arr):
    
        
    res = []
    if len(arr) == 1: return [0]
    if len(arr) == 0: return []
    
    l, r = 0, 1
    while l < r and r < len(arr):
        if arr[r] - arr[l] > 0: 
            #res.append(r-l)
            for i in range(r-l):
                res.append(r-(l+i))
            l += r-l
            r = l+1
        else: r += 1
            
    for i in range(len(arr)-len(res)): res.append(0)
        
    return res

    