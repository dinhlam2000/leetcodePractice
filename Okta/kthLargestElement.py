def findKthLargest(nums: [], k: int) -> int:
    import heapq
    heap = list()
    heapq.heapify(heap)

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            # print(heap)

            heapq.heappop(heap)
            # print(heap)
    return heapq.heappop(heap)

from typing import List
def findKthLargest(nums: List[int], k: int) -> int:
    target = len(nums) - k
    import pdb; pdb.set_trace()
    def quickSelect(l, r):
        pivot_value, pointer = nums[r], l

        for i in range(l, r):
            if nums[i] <= pivot_value:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1
        nums[pointer], nums[r] = nums[r], nums[pointer]
        if pointer > target:
            return quickSelect(l, pointer - 1)
        elif pointer < target:
            return quickSelect(pointer + 1, r)
        else:
            return nums[pointer]

    return quickSelect(0, len(nums) - 1)
#use a heap and maintain the length of heap and get the head of heap eventually
print(findKthLargest(nums=[1,6,3,2,7,4],k=3))
print(hash('lam'))