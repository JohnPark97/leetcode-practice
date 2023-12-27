Okay so this sounds like another problem where we are trying to see how many numbers overlap between two lists. Easiest way to solve this in O(n) is to get all numbers of s in a map where `{size: occurrence}`

This will result in O(s) + O(g) 

uhhh why is g = [1,2,3] s = [4] returning 1? Shouldn't it be 0. Oh wow `which is the minimum size of a cookie that the child will be content with` That's convincing. 

So I changed my approach to sort the two lists then just use two pointers and iterate through an array. Runtime if O(nlogn) + O(n) Space is O(1)

Time spent 21 min