import random

class SelectSort:
    def sort(self, input_list):
        for i in range(len(input_list)):
            min_index = i
            for j in range(i + 1, len(input_list)):
                if input_list[min_index] > input_list[j]:
                    min_index = j
            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
        return input_list

def main():
    o = SelectSort()

    inputList = []
    randomNum = random.randint(10, 50)
    for i in range(10000):
        randomInt = random.randint(-100, 100)
        inputList.append(randomInt)

    print(inputList)
    print(o.sort(inputList))

# Main code
if __name__ == "__main__":
    main()