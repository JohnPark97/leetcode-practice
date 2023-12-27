So it looks like a sorting/heap problem. Sorting would require O(nlogn) RC which is okay. Though I have a thought, can I do this in O(n)? Why don't I have three pointers and a new array and do this:
- on first iteration, figure out the top three and hold their index in pointers 
- We then iterate through the new array that contains all the ranks and adjust the values. 

Two things, watch out for `0`s and remember that the scores are unique

Hmm it's not passing the tests and the values are weird. Ah shoot I'm storing an index to pointers but comparing them the the scores. ohhhh the answer needs to have the placement value not the value in string zzz

Let's refresh this. Can I do in place modification and try to do this? I can think of a brutal brute force way of sorting them O(nlogn) then store them in map then go through the array again. Try that first zz

Wow it beat 95% of people with RC of O(nlogn) + O(n). Lesson of the day. Just do it before worrying about optimizing

Time spent 23 min
