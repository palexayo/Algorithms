import random

from NonTrivSort.MergeSort.MergeSort import MergeSort


class BinarySearch:
    def search(self, inputList, expression):
        left = 0
        right = len(inputList) - 1

        while left <= right:
            middle = (right + (right - left)) // 2

            if(inputList[middle] == expression):
                return middle
            elif(inputList[middle] < expression):
                left = middle + 1
            else:
                right = middle - 1

def main():
    print("Hello")

    sort = MergeSort()
    BinarySearchObjc = BinarySearch()


    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(randomNum):
        randomInt = random.randint(-100, 100)
        inputList.append(randomInt)

    print(inputList)
    randomNumSearchExpression = random.randint(0, len(inputList) - 1)
    search = inputList[randomNumSearchExpression]
    sortedList = sort.sort(inputList)
    print(sortedList)
    print(search)
    print(BinarySearchObjc.search(sortedList, search))

# Main code
if __name__ == "__main__":
    main()