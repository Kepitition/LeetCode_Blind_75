#BRUTE FORCE APPROACH 292/312 test cases passed
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cevap = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!= j:
                    for k in range(len(nums)):
                        if i != k and j != k:
                            if nums[i] + nums[k] + nums[j] == 0:
                                cevap.append([nums[i],nums[k],nums[j]])
        unique_permutations = list({tuple(sorted(perm)) for perm in cevap})
        return unique_permutations



