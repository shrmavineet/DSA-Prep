class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num &= 0xffffffff

        hex_chars = "0123456789abcdef"
        result = ""

        while num:
            digit = num & 0xf
            result = hex_chars[digit] + result
            num >>= 4

        return result