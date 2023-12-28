okay so it's a circular integer array where the index goes from nums.length -1 to 0 it seems like.

So I will have to iterate through the `nums` array at least once, RC O(n) and I'm going to make an array for my answer so SC O(n) so far. 
- for each element, go through the array at most nums.length - 1 times and look for the number greater than itself. O(n * n)

Oh so python doesn't have a built-in loop thing similar to ruby where I can to .times in ruby. I would have to add the index to the inner loop to make it use as an iterating pointer

Okay that was a good brute force solution. The runtime is horrific though, let's make it better.

14.5 min

ugh GPT 3.5 is pretty bad with thorough explanations. I asked for thorough explanation for stack solution which is O(n) but it kept giving me weird answers where 1 is greater than 1 or something... Gonna implement it by myself. 

Brilliant... I need to loop from right to left of the array because we are looking for next greater element where next is going to the right side. So we need to go from right to left with the stack implementation because that's how we can find the next greater element reversely.

Most difficult problem so far. Some useful learnings:
- using stack to store indices of elements that is of interest especially when the problem asks for `next` elements
- using modulo is useful for circular indexes of an array
