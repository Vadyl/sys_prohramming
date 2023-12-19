def mergeSort(input_array):
    if len(input_array) > 1:

        mid = len(input_array) // 2
        right_array = input_array[:mid]
        left_array = input_array[mid:]


        mergeSort(right_array)
        mergeSort(left_array)

        i = 0
        j = 0
        k = 0


        while i < len(right_array) and j < len(left_array):
            if right_array[i] < left_array[j]:
                input_array[k] = right_array[i]
                i += 1
            else:
                input_array[k] = left_array[j]
                j += 1
            k += 1


        while i < len(right_array):
            input_array[k] = right_array[i]
            i += 1
            k += 1

        while j < len(left_array):
            input_array[k] = left_array[j]
            j += 1
            k += 1


input_array = [12, 11, 13, 5 ,6 ,7]
print(input_array)
mergeSort(input_array)
print("mergeSort res: " ,input_array)
