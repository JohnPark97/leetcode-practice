Sort it, find the middle value. If it's an even length array either left or right mid is fine. Then increment or decrement the values as needed. 

Okay so the above will take O(nlogn) + O(n) so the time isn't so great. Let's optimize

time spent so far 4:41

What is Quick-Select? Hmm not sure if I'll ever use it in interview settings.

Though Found another good solution where if the array is sorted, then I just have to iterate half the array length. that improved the runtime by a lot.

Looks like quick select is using quick sort and is used for getting k-th smallest element in an array. Best runtime is O(n) but the worst case is O(n^2) so sorting could be faster in many cases.