I'll sort the list first O(nlogn) this will allow me to choose the smallest element easily.

A thought came in. The highest number will be on the right side and the low number will be on the left. I just have to subtract the highest number by the small numbers ascending.

[0,1,3,5,5] then subtract 5 by 1, (I need to keep the former subtracted number handy and accumulate it) (5-1) - (3-1), then (5-1)-(3-1) by (5-1)-(3-1) <- this 5 is the fourth one.

If this works, this would be O(n) + O(nlogn) = O(nlogn)

This test case failed with the above logic `[1,2,3,5]` oh that's because I didn't subtract the later numbers with the accumulator. Ah I had to change all the reference to nums[i] into nums[i] - acc because they all need to be subtracted.

been 20 min ish 

The solution was good, but can I make it better than O(nlogn)?

See if using a map can solve this in one or two pass of the array.

Turns out this problem was to identify unique elements in the array. That's clever way of seeing this, how would I approach it next time that I can catch that? 🤔 Converting the List to Set and excluding 0 (TIL `- {0}`) and getting the set's length will do the trick. That will give RC O(n) and SC O(n). My solution is RC O(nlogn) and SC O(1)

```
Chat GPT:
If the algorithm using sorting is consuming more memory than other solutions that utilize a set, it's likely because sorting is an in-place operation, and it modifies the original list. This can lead to a higher memory usage as the sorting algorithm might need additional space for temporary storage or to handle the sorting process.

In contrast, using a set doesn't modify the original list and typically requires additional space proportional to the number of unique elements in the list.
```