import random

class MaxTeilSum:
    def findMaxSubArray(self, inputList):
        if (len(inputList) == 1):
            if (inputList[0] < 0):
                return 0
            else:
                return inputList[0]
        else:
            dividedListTouple = self.divide(inputList)
            maxLAndRTouple = self.conquer(dividedListTouple)
            rightBorderMax = self.getListLeftRightBorderMax(inputList, len(dividedListTouple[0]))
            leftBorderMax = self.getListRightLeftBorderMax(inputList, len(dividedListTouple[0]))
            maxsum = self.merge(maxLAndRTouple[0], maxLAndRTouple[1], rightBorderMax, leftBorderMax)
            return maxsum

    def divide(self, inputList):
        inputSize = len(inputList) // 2
        listLower = inputList[:inputSize]
        listUpper = inputList[inputSize:]

        return listLower, listUpper

    def conquer(self, inputTouple):
        listLeft = inputTouple[0]
        maxL = self.findMaxSubArray(listLeft)

        listRight = inputTouple[1]
        maxR = self.findMaxSubArray(listRight)

        return maxL, maxR

    def getListLeftRightBorderMax(self, list, splitSize):
        rightBorderMax = 0
        sum = 0

        for i in range(splitSize - 1, -1, -1):
            sum += list[i]
            if rightBorderMax < sum:
                rightBorderMax = sum
        return rightBorderMax

    def getListRightLeftBorderMax(self, list, splitSize):
        leftBorderMax = 0
        sum = 0

        for i in range(splitSize, len(list)):
            sum += list[i]
            if leftBorderMax < sum:
                leftBorderMax = sum
        return leftBorderMax

    def merge(self, maxL, maxR, rightBorderMax, leftBorderMax):
        maxsum = 0
        if maxL > maxR:
            if maxL > rightBorderMax + leftBorderMax:
                maxsum = maxL
            else:
                maxsum = rightBorderMax + leftBorderMax
        else:
            if maxR > rightBorderMax + leftBorderMax:
                maxsum = max
            else:
                maxsum = rightBorderMax + leftBorderMax
        return maxsum


def main():
    print("Hello")


o = MaxTeilSum()

inputList = []
randomNum = random.randint(10, 50)
for i in range(randomNum):
    randomInt = random.randint(-100, 100)
    inputList.append(randomInt)

print(inputList)
print(o.findMaxSubArray(inputList))

# Main code
if __name__ == "__main__":
    main()
