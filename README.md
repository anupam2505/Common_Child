# Common_Child

Given two strings aa and bb of equal length, what's the longest string (SS) that can be constructed such that it is a child of both? 

A string xx is said to be a child of a string yy if xx can be formed by deleting 0 or more characters from yy. 

For example, ABCD and ABDC has two children with maximum length 3, ABC and ABD. Note that we will not consider ABCD as a common child because C doesn't occur before D in the second string.

#Input format

Two strings, aa and bb, with a newline separating them.

Constraints

All characters are upper cased and lie between ASCII values 65-90. The maximum length of the strings is 5000.

#Output format

Length of string SS.

#Sample Input #0

HARRY
SALLY

#Sample Output #0

2
The longest possible subset of characters that is possible by deleting zero or more characters from HARRY and SALLY is AY, whose length is 2.

#Sample Input #1

AA
BB

#Sample Output #1

0
