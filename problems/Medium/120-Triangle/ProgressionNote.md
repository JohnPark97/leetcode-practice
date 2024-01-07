Interesting question. Let's approach with O(n) RC first. Let's start by going through each row and saving the minimum value's index. Good I got the iteration. However, this is not a solution because it doesn't account for the rule of going down the adjacent indexes. What would be the best approach to tell if this path is lower than another? Perhaps I should have another triangle array that contains the minimum of each index. For example, I would put `5` for the first row first element as `2 -> 3` is lower than `2 -> 4`.Hmm I'm realizing that this approach is no good as it's the same as not adding the min values... I'm thinking of backtracking with depth first search. Well that's not easy with 2D array. Way different than I used nodes. 

Ah so I have been very close to a working version of dfs, just had to return min of right and left. However, it's exceeding time limit ;( So it was a dynamic programming for sure, because it can be broken down into sub problems for sure. The Bottom up approach really got me here. Wow brilliant so we keep summing to the top and it will give the answer haha what a genius idea. Always think of other way around is the moral of this problem.