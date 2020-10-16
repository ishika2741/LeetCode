class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted = nums.copy()
        sorted.sort()
        n = len(nums)
        ans = []
        for i in range(n-1):
            for j in range(i+1,n):
                if (sorted[i]+sorted[j] == target):
                    if (sorted[i] != sorted[j]):
                        ans.append(nums.index(sorted[i]))
                        ans.append(nums.index(sorted[j]))
                        return(ans)
                    else:
                        ans.append(nums.index(sorted[i]))
                        nums.remove(sorted[i])
                        ans.append(nums.index(sorted[j])+1)
                        return(ans)
                elif(sorted[i]+sorted[j]>target):
                    break
        sorted = nums.copy()
        sorted.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if (sorted[i] + sorted[n] == target):
                if (sorted[i] != sorted[n]):
                    ans.append(nums.index(sorted[i]))
                    ans.append(nums.index(sorted[n]))
                    return(ans)
                else:
                    ans.append(nums.index(sorted[i]))
                    nums.remove(sorted[i])
                    
                    
        
