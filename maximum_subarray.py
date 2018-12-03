#!/usr/bin/python

#Kadane dynamic programming

list =  [0,2,3,10,23,-9]
list = [10,14,52,-2,10,-22,-40,-3,11];

def maximum_subarray(A):
    
    max_end = max_until= A[0]

    for x in A[1:]:
        max_end = max(x, max_end + x)
        max_until = max(max_until, max_end)

    return max_until

max_value = maximum_subarray(list)

print max_value


