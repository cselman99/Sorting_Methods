import random
import time

def selection_sort(alist):
    alist_size = len(alist)
    comparisons = 0
    for x in range(alist_size):
        max_in = 0
        for y in range(1, alist_size - x):
            if alist[max_in] < alist[y]:
                max_in = y
            comparisons += 1
        alist[alist_size - x - 1], alist[max_in] = alist[max_in], alist[alist_size - x - 1]
    return comparisons

    
def insertion_sort(alist):
    alist_size = len(alist)
    comparisons = 0
    for i in range(1, alist_size):
        j = i - 1
        val = i
        larger = False
        for j in range(i - 1, -1, -1):
            if not larger:
                comparisons += 1
                if alist[val] < alist[j]:
                    temp = alist[val]
                    alist[val] = alist[j]
                    alist[j] = temp
                    val = j
                else:
                    larger = True
    return comparisons


def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 1000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()


