import random


class MaxTeilSum:
    def findMaxSubArray(self, inputList):
        # Base case: single element
        if len(inputList) == 1:
            return inputList[0]

        # Divide the list
        mid = len(inputList) // 2
        left_list = inputList[:mid]
        right_list = inputList[mid:]

        # Conquer step
        max_left = self.findMaxSubArray(left_list)
        max_right = self.findMaxSubArray(right_list)

        # Find max crossing sum
        max_cross = self._maxCrossingSum(inputList, mid)

        # Return the maximum of the three
        return max(max_left, max_right, max_cross)

    def _maxCrossingSum(self, inputList, mid):
        # Left of mid
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid - 1, -1, -1):
            current_sum += inputList[i]
            if current_sum > left_sum:
                left_sum = current_sum

        # Right of mid
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid, len(inputList)):
            current_sum += inputList[i]
            if current_sum > right_sum:
                right_sum = current_sum

        return left_sum + right_sum


def main():
    o = MaxTeilSum()
    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(randomNum):
        randomInt = random.randint(-100, 100)
        inputList.append(randomInt)

    print("Input List:", inputList)
    print("Maximum Subarray Sum:", o.findMaxSubArray(inputList))


if __name__ == "__main__":
    main()