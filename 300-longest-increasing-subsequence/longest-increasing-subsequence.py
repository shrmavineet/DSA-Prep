class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            # Find first element >= num
            pos = bisect_left(tails, num)

            if pos == len(tails):
                # num is greater than all elements
                tails.append(num)
            else:
                # Replace existing value
                tails[pos] = num

        return len(tails)