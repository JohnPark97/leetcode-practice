Haven't done Binary in ages, but let's try. I vaguely remember that binary trees usually involves recursive due to it's nature of branched structure.

I made an approach where I would iterate through bst and record everything in dict. Then I sort it and filter it by max value. That's suuuuuper expensive. Let's optimize this.

Learning: list comprehension in python [ key for key, value in map.items() if ...]

16 min spent

Well spent another 13 min to figure out what the solution was. The optimal solution even without hashmap was to iterate over the whole bst with dfs and have an in order list of values ready. Then we iterate over the in order list and it's a O(n) from there to find the max numbers