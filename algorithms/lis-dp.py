# User function Template for python3


class Solution:

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        # code here

        highest = 1
        LIS = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if a[i] < a[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence(a, n))
# } Driver Code Ends
