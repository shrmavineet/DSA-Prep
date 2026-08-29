class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        s = list(s)
        indexes = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                indexes.append(i)

        if len(indexes) != 2:
            return False

        i, j = indexes

        s[i], s[j] = s[j], s[i]

        return "".join(s) == goal