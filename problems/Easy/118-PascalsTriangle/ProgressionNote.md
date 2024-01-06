Okay, can I approach this with O(n) where I just go through each rows and try to get the previous row? Looks like the next row value will always get the previous row's `row[i] + row[i-1]`. Let's give that a try first. That was straight forward with O(n) approach

time taken: 12:51

Though this seems like it could be done in tree? O(logn). Nope it was dynamic programming like Fibonacci numbers