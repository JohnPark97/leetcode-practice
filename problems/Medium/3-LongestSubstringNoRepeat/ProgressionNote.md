So for the example "abcabcbb" I would go through the string from the beginning and record the non-repeating substring. When the iteration reaches the second "a", then it will have to be moved to the index after the duplicate entry

I solved it by using string.index() method in Python. This method takes in a character and will return an index of that character inside the string. Similar solution as the solution 3 of using map, I decided to just not use the map and just use the index from this method. 

Time taken: 10:09 min