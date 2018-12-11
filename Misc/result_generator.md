# Result Generator

## Program: [result_generator.py](https://github.com/nirantak/Programming_Exercises/blob/master/Misc/result_generator.py)

## Problem Description

In a programming competition, U number of users have qualified for the finale. The team has decided to ask P number of problems in finale with different problem score (S) and number of test cases (T), based on complexity of the problem.
The problem IDs will be alphabetic equivalent from A, B, C and so on, for problems 1 to P, where first problem will have problem Id as A, second will have problem Id as B and so on..
Any user may submit a problem multiple times. When a submission is done, all test cases for the problem are tried, and a result given for each test case.
Each test case will end up in any one of the six below mentioned statuses.

---
| Status Code | Explanation       |
| ----------- | ----------------- |
| A           | Accepted          |
| ML          | Memory Limit      |
| TL          | Time Limit        |
| WA          | Wrong Answer      |
| RT          | Runtime Error     |
| CE          | Compilation Error |
---

A problem will be considered as solved,if and only if all test cases for that problem have status "Accepted".

For each problem, a user will get a full score or a partial score. He will get a full score (=Problem score) if there is at least one submission where all test cases are in "Accepted" status. For each problem, a user will get a partial score for the submission for that problem which has the highest number of test cases in the "Accepted" status. The partial score given is score (problem score / number of test cases) for all test cases that end up with status "Accepted".

After the finale, next task of the team is to declare the result. The result is list of user who solved at least one test case of any problem, posed in the contest in descending order of Full Score and then Partial Score. Note that if only users who have at least one test case of any problem in the "Accepted" state, can be in the list.And if two or more users have tied for the same rank, give same rank to all and sort them in ascending order on their userid and next user's rank will be far away same number from them.

Suppose userid 34 and 45 have tied for 1st rank. Both of them placed for first rank and next user's rank will be 3rd.

Ex: 1 34 100 30
1 45 100 30
3 30 50 80
Help the team to declare result for the finale.

## Constraints

P <=26
1<U<=10000
1< Su<=10000

## Input Format

First line contains total number of problems (P) in the Finale

Next P lines contains 3 space delimited integers denoting problem ID, problem score (S) and number of test cases for that problem (T)

Next line contains 2 space delimited integers denoting number of finalists (U) and total submissions by all finalists (Su) in the Finale.

Next Su lines contain space delimited integers denoting userid, problem ID, submission ID and status code for each test case in the problem delimited by space.

## Output

Print the list of the users with their rank, userid, Full Score and Partial Score (two place of decimal) delimited by space in ascending order of their rank.

## Test Cases

### Example 1

#### Input 1

4
A 30 4
B 30 7
C 100 6
D 200 6
2 8
1 A 1 WA A TL A
2 D 1 WA A TL A A ML
2 D 2 RT WA TL A A A
1 C 2 WA RT TL A ML RT
2 C 3 A A TL A A A
1 C 4 A A A A A A
2 A 3 A A TL WA
2 D 4 A A A A A A

#### Output 1

1 2 200 98.33
2 1 100 15.0

#### Explanation 1

First 5 lines of input depict that there are 4 problems in finale viz. A, B, C and D. Their scores are 30, 30, 100 and 200 respectively. Number of test cases for each of them is 3, 7, 6 and 6 respectively.
Sixth line indicates that there are 2 finalists and together they have made 8 submissions.
Next 8 lines denote who has submitted solution to which problem and the corresponding status.
Upon crunching the data it turns out that userid 2 has topped the Finale by scoring 200 points as Full Score and 98.33 points as Partial Score. Userid1 is ranked at #2 and his Full Score is 100 and Partial Score is 15.

### Example 2

#### Input 2

2
A 250 11
B 200 9
5 15
3 B 1 TL ML WA WA WA WA WA A TL
3 B 2 ML WA ML A WA A TL ML RT
2 A 1 TL A RT ML ML A ML ML RT RT ML
0 A 1 TL RT ML RT A TL ML A RT RT A
1 A 1 A ML A A WA RT RT ML WA RT WA
2 A 2 A ML TL RT A WA ML A A TL RT
4 B 1 ML TL A TL A A WA RT ML
1 B 2 RT RT WA RT TL RT WA TL A
0 B 2 RT TL TL A A A RT TL ML
1 A 3 TL WA ML TL ML ML ML TL TL TL RT
2 A 3 A A A A A A A A A A A
0 B 3 TL RT A A WA A ML WA ML
4 A 2 A WA TL RT WA ML WA RT A WA RT
3 A 3 A A A A A A A A A A A
4 A 3 TL ML WA TL TL RT WA A A WA WA

#### Output 2

1 3 250 44.44
2 2 250 0.0
3 0 0 134.85
4 4 0 112.12
5 1 0 90.4

#### Explanation 2

First 3 lines of input depict that there are 2 problems in finale viz. A, and B. Their scores are 250 and 200 respectively. Number of test cases for each of them is 11 and 9 respectively.
Sixth line indicates that there are 5 finalists and together they have made 15 submissions.
Next 15 lines denote who has submitted solution to which problem and the corresponding status.
Upon crunching the data it turns out that userid 3 has topped the Finale by scoring 250 points as Full Score and 44.44 points as Partial Score. Userid 2 is ranked at #2 and his Full Score is 250 and Partial Score is 0.0 and so on.
