# Spiral Primes

## Problem Description

The prime numbers are written in a spiral form staring at (0,0) and moving as shown in the diagram below.

The objective is to find the prime at a given position (x and y coordinates)

## Constraints

N <= 20

Each output prime < 1000000

-130 < x,y < 130

## Input Format

The first line has an integer N that specifies the number of coordinates in this test case

The next N lines each have a pair of comma separated integers, which are the x and y coordinates of the position 

## Output

The output consists of N lines.

Each consists of an integer specifying the prime at the corresponding position.

## Explanation

### Example 1

#### Input 1

2  
1,0  
0,1

#### Output 1

3  
7

#### Explanation 1

N=2. There are 2 sets of coordinates in this test case. The coordinates are (1,0) and (0,1). The corresponding primes in the spiral are 3 and 7. The output hence has these.

### Example 2

#### Input 2

3  
1,1  
-1,1  
-1,0

#### Output 2

5  
11  
13

#### Explanation 2

There are 3 sets of coordinates in this test case (N=3). The coordinates are (1,1),(-1,1) and (-1,0). The corresponding primes at these positions are 5, 11, 13. Hence the output has these 3 lines.
