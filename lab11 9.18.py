def in_order(nums):
    # Iterate through the list to check if it's in descending order
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            return False
    return True

if __name__ == '__main__':
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In descending order')
    else:
        print('Not in order')
        
    nums2 = [10, 8, 7, 6, 5]
    if in_order(nums2):
        print('In descending order')
    else:
        print('Not in order')
