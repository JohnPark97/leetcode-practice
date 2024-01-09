Hmm two pointer sounds like the easiest solution along with using a map perhaps. So I initially go thorugh the whole `s1` first and map all the occurrences of the characters in `s1`. Then I go through the second string and check two things:
- are all the character occurrences the same? 
- How many letter positions are different?

RC = O(2n) SC = O(n)
SC = O(n)

Can I make this better? TIL there is a `zip` iterator in python where one can iterate over multiple lists in one iteration. It puts each iteration in a tuple

Time spent: 13 min