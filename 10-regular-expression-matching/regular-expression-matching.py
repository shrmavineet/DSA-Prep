class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):

            # If pattern is finished
            if j == len(p):
                return i == len(s)

            # Check whether current characters match
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == '.')
            )

            # If next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                
                # Option 1: use '*' zero times
                skip = dfs(i, j + 2)

                # Option 2: use '*' one or more times
                use = first_match and dfs(i + 1, j)

                return skip or use

            # Normal character or '.'
            if first_match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)