#Instructions:
'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''

#My Original Solution:
'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        combined = []
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
           combined.append(word1[i])
           i += 1
           combined.append(word2[j])
           j += 1
        while i < len(word1):
            combined.append(word1[i])
            i += 1
        while j < len(word2):
            combined.append(word2[j])
            j += 1
        return ''.join(combined)
'''
#Refactored Solution:
class Solution(object):
    def mergeAlternately(self, word1, word2):
        combined = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                combined.append(word1[i])
            if i < len(word2):
                combined.append(word2[i])
            i += 1
        return ''.join(combined)

#Test Cases:
'''
Test Case 1:
word1 =
"abc"
word2 =
"pqr"

Test Case 2:
word1 =
"ab"
word2 =
"pqrs"

Test Case 3:
word1 =
"abcd"
word2 =
"pq"
'''

#Results:
'''
Test Case 1:
Input
word1 =
"abc"
word2 =
"pqr"
Output
"apbqcr"
Expected
"apbqcr"

Test Case 2:
Input
word1 =
"ab"
word2 =
"pqrs"
Output
"apbqrs"
Expected
"apbqrs"

Test Case 3:
Input
word1 =
"abcd"
word2 =
"pq"
Output
"apbqcd"
Expected
"apbqcd"
'''