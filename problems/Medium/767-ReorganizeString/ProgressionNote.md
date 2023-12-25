So basically no duplicates side by side. If not return null. This indicates to me that we can check some kind of condition where _If there exists a character that is more than half length of the string_ we are going to throw "".

Thing that comes into my mind is to store everything in the map then we shuffle the string so it doesn't have repeating characters. 

- go through the string and store each characters in a map
- map will contain a character as a key and occurrence as a value `{#{char}: #{occur}...}`
- whenever we insert, we will check to see if the occurrences are more than half length of the string
	- If the above condition passes we can re organize
	- I want to have a new string that I'm going to reorganize... If a character repeats, I need to store it somewhere (stack?)

Got this part done `- whenever we insert, we will check to see if the occurrences are more than half length of the string`.
Hmm I thought of making a carry over data structure as a stack first than changed to string and realized that there could be multiple carryovers in case of `aaaaaabbbb` so back to maps... stuck though something doesn't align.

Get the key value pairs, now I need to somehow keep concatnating the highest occurrence string every other iteration. Should I just not care about runtimes, thinking of ordering the dictionary by values 

Completely stuck, using GPT for hints. It told me to use the greedy algorithm approach. Greedy algorithm is for me to choose what is the best solution at each step/iteration without thinking about the bigger performance and space complexity stuff. With a descending map, what can I do... 

Looked at the answer key. Wow I actually thought of the second approach to go even first then to go odd. Did it, it turned out to be O(n) to go through the string to put them in a map, sort them O(nlogn) descending then go through the items in map to create a new string O(n). Overall O(n) + O(n) + O(nlogn)

Love the GPT solution. TIL There is a built in Counter in python where given a string it creates a map-like Counter object that contains all the occurrences of characters. Though I'm going to post my own solution for future reference. When I get back to it, see if I can optimize it.