## Dec 24

Initial thought:

Have a map that stores past numbers and go through the map of keys a
map will be {#{num}: #{index}}

let's sort it first O(nlogn) then try.
I'm currently stuck on having a negative number uggghhhhh 
[-3, 4, 3, 90] target = 0
sorting it becomes [-3, 3, 4, 90] what's next? 
instead of using a map, why don't I start simple and just have a pointer to iterate the whole array. Let's not care about optimization

So sorting was a bad idea as I had to give an answer in original indexes lol

I changed my method so I would just go over the array and go over the array while pointing to a particular index. This approach resulted in O(n^2) in which I'm not satisfied as a solution for an "_EASY_" problem. 

So I turned back to my map idea, even though there will be a O(n) space complexity I couldn't think of a way to solve this problem in O(1) SC so I'm just going to try.

I managed to go through the whole list once and store the numbers with index `{#{num}: #{index}}`. It was a satisfying success and the runtime was O(2n) and O(n) SC. Of course there was a one pass solution in LeetCode but I'm satisfied to be able to solve this problem while thinking through.

Time spent: 40 min in total