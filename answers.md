# CMPS 2200 Assignment 3
## Answers

**Name:**_________________________


Place all written answers from `assignment-03.md` here for easier grading.

1a. Find the higest denomiations of coins possible as long as 2^k <= N. As long as the current denomiation is <= N, subtract it from N until N = 0.

1b. If you select the highest denomination of coin to be used at each iteration, you can ensure that you use the least amount of coins throughout the whole function. 

1c. The work and span are O(log(n))

2a. With Fortuito currency the greedy algorithm would likely sellect a 4 dollar coin and 2 one dollar coins. But the optimal solution is 2 three dollar coins. In this sense, it is a counter example to the optimal solution.

2b. Using recursive calling the algorithm can determine the optimal denomination counts for each coin. Since it is calcuating the fewest demonations we also get the answer to the optimal solution for all N.

2c. The work and span would be O(N*) and O(k)