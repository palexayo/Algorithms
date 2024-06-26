import random

class BubbleSort:
    def sort(self, inputList):
        for i in range(0, len(inputList)):
            for j in range(0, len(inputList) - i - 1):
                if(inputList[j] > inputList[j + 1]):
                    inputList[j + 1], inputList[j] = inputList[j], inputList[j + 1]
        return inputList


def main():
    o = BubbleSort()

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