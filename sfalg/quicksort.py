import random

def quicksort(myList):
	if len(my>List) < 2:
		return myList
	pivot = random.choice(myList)
	left = []
	right = []
	middle = []
	for x in myList:
		if x < pivot:
			left.append(x)
		if x > pivot:
			right.append(x)
		if x == pivot:
			middle.append(x)
	left =  quicksort(left)
	right = quicksort(right)
	return left + middle + right

