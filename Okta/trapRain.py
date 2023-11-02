class Solution:
    def trap(self, height: List[int]) -> int:
        # keep track of the max height to the left = maxLeft
        # keep track of the max height to the right = maxRight
        # MATH PART:
        # we know that we can only trap so that water won't pour out
        # water will pour out if one side is less than the other
        # THEREFORE, for each index, we can only trap water up to the height of either the height on left or height on right
        # we can trap water up to the smaller height
        # so we know that we can take a look at the current min(maxLeft and maxRight) - current height -> trapped Water
        # then if trapped Water > 0 -> that's the amount of water we trap
        maxLeft = []
        maxRight = []

        for i in range(len(height)):
            if i == 0:
                maxLeft.append(height[i])
                maxLeftValue = height[i]
            else:
                maxLeft.append(maxLeftValue)
                maxLeftValue = max(height[i], maxLeftValue)

        for j in range(len(height) - 1, -1, -1):
            if j == len(height) - 1:
                maxRight.append(height[j])
                maxRightValue = height[j]
            else:
                maxRight.insert(0, maxRightValue)
                maxRightValue = max(height[j], maxRightValue)
        result = 0
        print(maxLeft, maxRight)
        for index, h in enumerate(height):
            trappedRain = min(maxRight[index], maxLeft[index]) - h
            print(trappedRain)
            if trappedRain > 0:
                result = result + trappedRain
        return result