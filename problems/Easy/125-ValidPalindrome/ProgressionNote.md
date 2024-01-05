I initially was going to use a straight forward 
```
alnum_str = ''.join(char for char in s if char.isalnum()).lower()
```

This is a very straight forward answer where the run time is O(len(s) * 2) as we go through the string twice. So I wanted to improve on top of that. I wanted to try to do in O(len(s)). 

So I would iterate each pointer to the next alphanumeric number in each iteration then check if left and right are still lower and higher then one another. If they are not, that means that they have checked everything and they all matched(or they were non-alpha numerics that we take as valid palindrome)

Time taken: 20 min