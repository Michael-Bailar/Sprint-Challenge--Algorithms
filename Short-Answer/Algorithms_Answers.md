#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) our while loop is n^3 and our condition is n^2. 
    dividing n^3 by n^2 always gives us n. This brings our complexity down to O(n).


b) This problem looks like it coud be fairly linear
    until you look at the j *= 2 line which is log(n).
    Since the loop keeps resetting past the point where j = n in a linear fashion, I would call this
    O(n + log(n)) time.

c) this simply adds 1 operation every time you 
    increase the input by 1. I would call this O(n) time. But it's more efficient than nmost O(n) 
    times that I've seen.

## Exercise II

So in this problem, I am assuming we are trying to find f given n. I think it's pretty straight forward.

Given N
declare a middle variable
declare abreak height variable
set middle variable to n//2
run test at middle(drop the egg from this height)
if middle is equal to the break height
    return middle.
else if the egg breaks
    pick a height halfway between middle and bottom
    set break height to middle
    set middle to the new middle
else the egg doesn't break
    pick a height halfway between (middle + 1 )and top
    set middle to that
