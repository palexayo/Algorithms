import random

class HeapSort:
    def sort(self, inputList):
        self.maxHeap(inputList)

        sortedList = []

        for i in range(len(inputList) - 1, 0, -1):
            inputList[0], inputList[i] = inputList[i], inputList[0]
            sortedList.append(inputList.pop())
            self.maxHeapify(inputList, i, 0)
        sortedList.append(inputList[0])
        return sortedList[::-1]

    def maxHeapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.maxHeapify(arr, n, largest)

    def maxHeap(self, arr):
        """
        Build a max heap from the given array
        """
        n = len(arr)
        # Build max heap starting from the last non-leaf node and moving up to the root
        for i in range(n // 2 - 1, -1, -1):
            self.maxHeapify(arr, n, i)


def main():
    print("Hello")

if __name__ == "__main__":
    o = HeapSort()
    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(10):
        randomInt = random.randint(-100, 100)
        inputList.append(randomInt)

    print(inputList)
    print(o.sort(inputList))
