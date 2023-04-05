class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
    
test=Solution()

print(test.singleNumber([2,2,1]))
print(test.singleNumber([4,1,2,1,2]))
print(test.singleNumber([1]))