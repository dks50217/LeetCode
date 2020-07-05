class Demo():
    ##2020/6/13
    def twoSum(self,nums:'List[int]',target:'int') -> 'List[int]':
        numsMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numsMap:
                return [numsMap.get(target-nums[i]),i]
            else:
                numsMap[nums[i]] = i
        return [-1,-1]
    def validAnagram(self,s:str,t:str) -> bool:
        if len(s)!=len(t):return False
        cntDir = {}
        for c in s:
            print(c)
            #if cntDri can not get [c] and set value to 0 + 1
            cntDir[c] = cntDir.get(c,0) + 1
        #print(cntDir)
        for c in t:
            if c not in cntDir or cntDir[c] == 0:
                return False
            else:
                cntDir[c] -= 1 
        #print(cntDir)    
        return True
    def searchInsert(self,nums:'List[int]',target:'int') -> 'int':
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low

d = Demo()
nums = [11,15,7,2]
target = 9
print(d.twoSum(nums,target))

str1 = 'cat'
str2 = 'tca'
print(d.validAnagram(str1,str2))

_searchInsertList = [1,3,5,6]
target = 10
print(d.searchInsert(_searchInsertList,target))





