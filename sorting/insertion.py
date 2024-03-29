def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:

            array[j + 1] = array[j]
            j = j - 1;
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
        print(array)

data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)