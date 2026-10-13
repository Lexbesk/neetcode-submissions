class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1))] for j in range(len(text2))]
        if not text1 or not text2:
            return 0
        for i in range(len(text2)):
            for j in range(len(text1)):
                if i == j == 0:
                    dp[i][j] = 1 if text1[0] == text2[0] else 0
                elif i == 0:
                    dp[i][j] = 1 if (dp[i][j-1] == 1 or text1[j] == text2[i]) else 0
                elif j == 0:
                    dp[i][j] = 1 if (dp[i-1][j] == 1 or text1[j] == text2[i]) else 0
                else:
                    num1 = 0
                    if i - 1 >= 0 and j - 1 >= 0 and text1[j] == text2[i]:
                        num1 = dp[i-1][j-1] + 1
                    num2 = dp[i-1][j] if i - 1 >= 0 else 0
                    num3 = dp[i][j-1] if j - 1 >= 0 else 0
                    dp[i][j] = max(num1, max(num2, num3))
        return dp[-1][-1]