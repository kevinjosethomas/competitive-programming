# User function Template for python3

import bisect


class Solution:

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        # code here

        length = 1
        LIS = [a[0]]

        for i in range(1, n):
            if a[i] > LIS[-1]:
                LIS.append(a[i])
                length += 1
            else:
                index = bisect.bisect_left(LIS, a[i])
                LIS[index] = a[i]

        return length

        # User function Template for python3


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(1):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence(a, n))
# } Driver Code Ends
