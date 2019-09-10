import random
import time
from demos import quicksort, mergesort


def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

size = int(input("What size list would you like to create? Enter a number: "))
max = int(input("What is the maximum value of the list you are creating? "))

l = create_random_list(size, max)
tic = time.time()
quicksort(l)
toc = time.time()
print("QuickSort Elapsed time -> ", toc-tic)

tic = time.time()
mergesort(l)
toc = time.time()
print("MergeSort Elapsed time -> ", toc-tic)
