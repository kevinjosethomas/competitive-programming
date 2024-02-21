# User function Template for python3


class Solution:

    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, x, y, s1, s2):

        matrix = [[0 for __ in range(len(s1) + 1)] for __ in range(len(s2) + 1)]

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    matrix[i][j] = 1 + matrix[i + 1][j + 1]
                else:
                    matrix[i][j] = max(matrix[i][j + 1], matrix[i + 1][j])

        print(matrix)

        return matrix[0][0]


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == "__main__":
    test_cases = 1
    for cases in range(test_cases):
        x, y = map(int, input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob = Solution()
        print(ob.lcs(x, y, s1, s2))
# } Driver Code Ends
