import random

class InsertionSort:
    def sort(self, inputList):
        for i in range(1, len(inputList)):
            key = inputList[i]
            j = i - 1
            while key < inputList[j] and j >= 0:
                inputList[j + 1], inputList[j] = inputList[j], inputList[j + 1]
                j -= 1
        return inputList

    def euklid(self, a, b):
        i = 1
        while not a == b:
            print(i)
            i += 1
            if b > a:
                tmp = a
                a = b
                b = tmp
            a = a - b
        return a

def main():
    o = InsertionSort()

    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(randomNum):
        randomInt = random.randint(-100, 100)
        inputList.append(randomInt)

    print(o.euklid(35, 15))

# Main code
if __name__ == "__main__":
    main()
