import random

class MergeSort:
    def sort(self, inputList):
        if len(inputList) == 1:
            return inputList

        half = (len(inputList) / 2).__round__()

        listLeft = self.sort(inputList[:half])
        listRight = self.sort(inputList[half:])

        indexLeft = 0
        indexRight = 0

        sortedList = []
        while indexLeft < len(listLeft) and indexRight < len(listRight):
            if listLeft[indexLeft] < listRight[indexRight]:
                sortedList.append(listLeft[indexLeft])
                indexLeft += 1
            else:
                sortedList.append(listRight[indexRight])
                indexRight += 1

        sortedList.extend(listLeft[indexLeft:])
        sortedList.extend(listRight[indexRight:])

        return sortedList

def main():
    o = MergeSort()

    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(randomNum):
        randomInt = random.randint(-100, 100)
        inputList.append(randomInt)

    print(inputList)
    print(o.sort(inputList))

# Main code
if __name__ == "__main__":
    main()