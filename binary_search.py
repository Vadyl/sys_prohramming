
def binary_search(arr, l, r, value):
	if r >= l:

		mid = (r + l) // 2


		if arr[mid] == value:
			return mid

		elif arr[mid] > value:
			return binary_search(arr, l, mid - 1, value)

		else:
			return binary_search(arr, mid + 1, r, value)

	else:

		return -1

arr = [ 1, 2, 3, 8, 10 , 1000 ]
value = 10

res = binary_search(arr, 0, len(arr) - 1, value)


print("Element is present at index(-1 if dont): ", str(res))

