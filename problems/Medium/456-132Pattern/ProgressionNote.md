Okay.... So the brute force will be pretty brutal where I have three pointers and iterate each pointers one by one. Can I use stack maybe?
i'll just try the three pointer method first

ofc time limit exceeded because of the O^3 Runtime. That's really tragic runtime for sure. 

Okay using a stack has worked but I had to cheat and use chatGPT for help. Debugging and looking at the step by step, this seems like the solution:
- have a variable to store the number that represents `2`
- stack represents the numbers that have been visited. They are only popped and set as `2` if the current number is greater than the top of the stack. This fulfills the `32` pattern.
- Then if the next iteration is less than second, then we know for sure that there exists a `132` pattern. 

I had a brief idea of using stack but I couldn't completely utilize and capitalize my understanding. Next time hope I can nail these ones.