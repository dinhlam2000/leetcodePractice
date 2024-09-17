class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # for each worker, find the job with the max profit
        # in order to do that

        # brute force
        # for each worker,  find its ability --> WORKERaBILITY
        # find all the jobs that have difficulty level under WORKERABILITY and find max profit from all those jobs
        # add to result

        # OPTIMIZE THIS
        # Sort the difficulty and assign the max profitable up to that point
        # since difficulty is sorted, we can do this
        # e.g diff = [1,2], profit = [99,3] --> sorted = [(1,99), (2,99)]
        # once we have this sorted
        # look at each worker's ability and perform a binary search to find the max index of difficulty it can perform
        sortedDifficultyProfit = []
        for i in range(len(difficulty)):
            sortedDifficultyProfit.append((difficulty[i], profit[i]))

        sortedDifficultyProfit = sorted(sortedDifficultyProfit, key=lambda x: x[0])
        max_profit = sortedDifficultyProfit[0][1]
        for i in range(1,len(sortedDifficultyProfit)):
            max_profit = max(max_profit, sortedDifficultyProfit[i][1])
            sortedDifficultyProfit[i] = (sortedDifficultyProfit[i][0], max_profit)
        result = 0
        print(sortedDifficultyProfit)
        for ability in worker:
            maxIndex = self.binarySearch(ability, sortedDifficultyProfit)
            print(ability,maxIndex)
            if maxIndex != -1:
                result = sortedDifficultyProfit[maxIndex][1] + result

        return result

    def binarySearch(self,ability,difficulties):
        left = 0
        right = len(difficulties)
        result = 0
        if ability < difficulties[0][0]:
            return -1
        while left < right:
            # start with the left index + right index
            # look at center -->
            # if difficulty > ability
            # set right to be center - 1
            # if difficulty < ability
            # result could be that index but lets keep searching!
            center = (right + left) // 2
            # print(center, right,left)
            if difficulties[center][0] > ability:
                right = center
            else:
                result = center
                left = center + 1


        return result
