class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list2 = []
        flag = False
        for num in nums:
            if num in list2:
                flag = True
                break
            else:
                list2.append(num)
                flag = False
        return flag