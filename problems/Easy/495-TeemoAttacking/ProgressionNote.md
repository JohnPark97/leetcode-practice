This sounds like finding an overlap and minus that to the total duration. So how can we find an overlap? Simple just go through the array and see if the next point of time is greater than the current point of time + duration - 1

well that worked zz. Can I make it quicker? It's currentl O(n) at the moment... 

hmm not sure why mine is 50ms slower than this
```
class Solution:
    def findPoisonedDuration(self, A: list[int], duration: int) -> int:
        ans = 0
        for i in range(len(A) - 1):
            ans += min(duration, A[i + 1] - A[i])
        return ans + duration
```

Mine
```
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = duration
        for i in range(1, len(timeSeries)):
            ans += min(duration, timeSeries[i] - timeSeries[i-1])

        return ans
```