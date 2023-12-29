Well first grid problem honestly don't know what's the best approach runtime wise. The first thing I noticed is that for every `1` tile if there is a `1` beside it, we don't cound the perimeter. So for every `1`s, if we were to check it's adjacent tile and if it's 1 minus 1 from 4 and add all those numbers. 

Okay i'm catching all the edges, now just have to check if the adjacent if 0. Though have been getting some index out of range error hmm.. Ack mixed up the right, left and down, up. Right should be `j` and up should have been `i`. Mixed them up so the index kept going out of bounds. 

hmm so the run time is O(ij). Though it's so slow.. 

time spent 26 min