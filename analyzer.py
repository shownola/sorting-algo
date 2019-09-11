import random
import time
from demos import quicksort, mergesort, bubblesort


def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()}\t -> Elapsed time: {seconds} ")


size = int(input("What size list would you like to create? Enter a number: "))
max = int(input("What is the maximum value of the list you are creating? "))

l = create_random_list(size, max)

analyze_func(quicksort, l)
analyze_func(mergesort, l)
analyze_func(bubblesort, l.copy())
