# Coast Guard Problem

## Problem Description

Of late, smuggling has increased many fold and as Chief of the Coast Guard, you are responsible for intercepting the smuggling vessels and nullify them. You have stationed several smart, high speed boats in the sea. The entire sea under your control can be divided into a rectangular grid of 1 km by 1 km squares. Due to a design flaw in the boats, they can move only in horizontal or vertical directions (EW or NS) (they cannot move diagonally, in particular). Of course, no two boats are stationed in the same grid square.

The boats can reach an adjacent grid square (horizontally or vertically) in one minute. Every grid square that can be reached by one boat faster than it can be reached by any other boat is said to be controlled by that boat. If a grid square may be reached by at least one more boat in the same time as the fastest boat, it is said to be uncontrolled.

It is in your interest to minimize the number of grid squares that are uncontrolled.

In the figure above we are considering a grid of 3 rows and four columns. The bottom left corner square is numbered (0,0), and the top right corner is numbered (3,2). Two boats are in positions (2,0) and (0,2). The four shaded squares can be reached in equal (minimum) time by both boats, and are hence uncontrolled.

Given the position of the boats, write a program to identify the number of grid squares that are uncontrolled.

## Constraints

M>0, N<50, 1<k<10

## Input Format

The first line will be three comma separated integers M, N and k. M and N give the number of rows and columns of the grid, and k the number of boats.

The next k lines will a pair of comma separated numbers giving the coordinates of the grid square with a boat

## Output

A single line containing the number of uncontrolled grid squares.

## Explanation

### Example 1

#### Input 1

3,4,2  
2,0  
0,2

#### Output 1

4

#### Explanation 1

M=3,N=4,k=2. There are 3 rows and 4 columns. There are 2 boats at (2,0) and (0,2).

The position is the same as in the earlier figure. There are 4 uncontrolled squares. Hence the result is 4.

### Example 2

#### Input 2

2,4,2  
0,1  
2,0

#### Output 2

0

#### Explanation 2

M=2, N=4, k=2. There are two boats positioned as below

It can be seen that there is no grid square that is reached at the same minimum time from the two boats. Hence the result is 0.
