## HW4

# 2 different sorting algorithms (ones from class just with different complexities)
# O(n^2) and O(nlogn)

#graph with -Vertical axis in time - Horizontal axis is N size of set to sort - one line for each algorithm = label everything
# https://visualgo.net/bn/sorting
# https://betterexplained.com/articles/sorting-algorithms/#Radix_sort_BestAvgWorst_ON

# Graphing in python https://plot.ly/python/

#bubble sort
#x=[4,2,1]


#index list of numbers [0]  [1].
#if [0] > [1] switch then repeat

#x[0]>x[1]

#BubbleSort

import random
random_l = random.sample(range(10), 10)

listn= [2,1,3]
def BubbleSort(listn):
	for i in range(0,len(listn)):
		for j in range(i+1, len(listn)): #range(1,len(listn)):
			if listn[i]>listn[j]:
				listn[i], listn[j] = listn[j], listn[i]
	return listn

BubbleSort(random_l)
BubbleSort(listn)



#Insert sort

def InsertSort(listn):
	for index in range(1,len(listn)):
		current = listn[index]
		while index >= 1 and listn[index-1]>current:
			listn[index]=listn[index-1]
			index+=-1
		listn[index] = current
	return listn
InsertSort(random_l)


# Not differect complexities

# selection sort


def SelectionSort(listn):


while i<len(listn):
    minim = min(listn[i:])
    minim_index = listn.index(minim)
    listn[i],listn[minim_index] = listn[minim_index],listn[i]
return (listn)
 





