class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for i in s:
            if i.isalnum():
                text += i.lower()
        s = text[::-1]

        i,j = 1,0
        while(j<=len(s)-1 and i == 1):
            if s[j] == text[j]:
                j += 1
            else:
                i = 0
        if i == 0:
            return False
        else:
            return True