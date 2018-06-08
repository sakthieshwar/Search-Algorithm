dataset1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
dataset2 = [0, 15, 30, 50, 60, 70, 80, 105, 231, 123123, 12312314]

## Linear Search Algorithm

def searchLinearly(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return 'The target is found at the index {}.'.format(i)
    return 'Target is not found.'

print('Linear Search Algorithm')
print(searchLinearly(dataset1, 16))
print(searchLinearly(dataset1, 99))
print(searchLinearly(dataset1, 23))
print()

## Binary Search Algorithm (Recursive)

def searchBinarily(data, target):
    
    index = 0
    dataset = data

    def getLength(inp):
        return len(inp)

    def getHalf(inp):
        return int(getLength(inp) / 2)

    def search(data, target, index):
        try:
            half = getHalf(data)
            
            if data[half] == target:
                return 'The target is found at the index {}.'.format(index + half)
            
            elif data[half] > target:
                return search(data[:half], target, index)

            else:
                index += half + 1
                return search(data[(half + 1):], target, index)
        except(IndexError):
            return 'Target is not found.'

    return search(dataset, target, index)

print('Binary Search Algorithm (Recursive)')
print(searchBinarily(dataset1, 2))
print(searchBinarily(dataset1, 5))
print(searchBinarily(dataset1, 8))
print(searchBinarily(dataset1, 12))
print(searchBinarily(dataset1, 16))
print(searchBinarily(dataset1, 23))
print(searchBinarily(dataset1, 38))
print(searchBinarily(dataset1, 56))
print(searchBinarily(dataset1, 72))
print(searchBinarily(dataset1, 91))
print(searchBinarily(dataset1, 99))
print(searchBinarily(dataset2, 232))
print(searchBinarily(dataset2, 231))
print()

## Binary Search Algorithm (Iterative)

def searchBinarily(data, target):
    '''to preserve the original data variable'''
    dataset = data

    def getLength(inp):
        return len(inp)

    def getHalf(inp):
        return int(getLength(inp) / 2)
    
    index = 0
    
    while True:
        try:
            half = getHalf(dataset)
                    
            if dataset[half] == target:
                return 'The target is found at the index {}.'.format(half + index)
            
            elif dataset[half] > target:
                dataset = dataset[:half]
            
            else:
                index += half + 1
                dataset = dataset[(half+1):]
        except(IndexError):
            return 'Target is not found.'

print('Binary Search Algorithm (Iterative)')
print(searchBinarily(dataset1, 2))
print(searchBinarily(dataset1, 5))
print(searchBinarily(dataset1, 8))
print(searchBinarily(dataset1, 12))
print(searchBinarily(dataset1, 16))
print(searchBinarily(dataset1, 23))
print(searchBinarily(dataset1, 38))
print(searchBinarily(dataset1, 56))
print(searchBinarily(dataset1, 72))
print(searchBinarily(dataset1, 91))
print(searchBinarily(dataset1, 99))
print(searchBinarily(dataset2, 232))
print(searchBinarily(dataset2, 231))
print()
