This feels like a math question alright. This is under two pointers + binary search. At the moment I'm not getting any sense of two pointer approach nor binary. Not thinking of performance, why don't I initially try to iterate `a` starting from 1 and try to get the `b` by `sqrt(c-a^2)`. When do I stop? When `a^2` is bigger than `c` 

Okay this approach worked for test cases like 5 and 3. Though it's failing for 0 and 13. Asked ChatGPT on how to keep the values to int because 13 was failing because `b` was returning a float value instead of `int`. It gave an amazing suggestion to keep the `b_squared` value as a variable and compare that to `int(b)` value. Worked! 

15 min spent

Can I optimize this?

Binary search sounds worse for this problem. My approach had RC O(sqrt(n)) but b_search is O(sqrt(n)log(sqrtn))

What is Fermat Theorem...
```
Any positive number n is expressible as a sum of two squares if and only if the prime factorization of n, every prime of the form (4k+3) occurs an even number of times.
```
Woot haha. 