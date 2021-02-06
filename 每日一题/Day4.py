def findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    max_sum = cur_sum = sum(nums[:k])
    lenth = len(nums)

    for i in range(k, lenth):
        cur_sum = cur_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, cur_sum)

    return 1.0 * max_sum / k