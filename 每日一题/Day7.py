def checkPossibility( nums):
    length = len(nums)
    
        if length <= 2:
            return  True
        
        count = 0;
        
        for i in range(1,length):
            if nums[i] < nums[i - 1]:
                count = count + 1;
                if i == 1 or nums[i] >= nums[i -2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                if count > 1:
                    return  False
        
        return True
    

