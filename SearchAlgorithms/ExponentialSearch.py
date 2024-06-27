import random

from NonTrivSort.MergeSort.MergeSort import MergeSort
from SearchAlgorithms.BinarySearch import BinarySearch

class ExponentialSearch:
    def search(self, inputList, expression):
        if(len(inputList) == 0):
            return -1
        if (inputList[0] == expression):
            return 0
        index = 1
        while(index < len(inputList) and inputList[index] < expression):
            index *= 2

        if(index >= len(inputList)):
            index = len(inputList) - 1

        left = index // 2
        right = index

        sublist = inputList[left:right]
        return left + BinarySearch.search(self, sublist, expression)
def main():
    print("Hello")

    sort = MergeSort()
    ExponentialSearchObj = ExponentialSearch()


    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(randomNum):
        randomInt = random.randint(-500, 500)
        inputList.append(randomInt)

    print(inputList)
    randomNumSearchExpression = random.randint(0, len(inputList) - 1)
    search = inputList[randomNumSearchExpression]
    sortedList = sort.sort(inputList)
    print(sortedList)
    print(search)
    print(ExponentialSearchObj.search(sortedList, search))

# Main code
if __name__ == "__main__":
    main()