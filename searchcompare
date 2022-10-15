import time
import random


def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end_time = time.time()
    executiontime = (end_time - start_time)
    return found, executiontime


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            stop = True
        else:
            pos = pos+1
    end_time = time.time()
    executiontime = (end_time - start_time)
    return found, executiontime


def binary_search_iterative(a_list, item):
    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    end_time = time.time()
    executiontime = (end_time - start_time)
    return found, executiontime


def binary_search_recursive(a_list, item):
    start_time = time.time()
    if len(a_list) == 0:
        end_time = time.time()
        executiontime = (end_time - start_time)
        return False, executiontime
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end_time = time.time()
        executiontime = (end_time - start_time)
        return True, executiontime
    elif item < a_list[midpoint]:
        end_time = time.time()
        executiontime = (end_time - start_time)
        return binary_search_recursive(a_list[:midpoint], item), executiontime
    else:
        end_time = time.time()
        executiontime = (end_time - start_time)
        return binary_search_recursive(a_list[midpoint + 1:], item), executiontime


def main():
    i = 1
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    randmlst = [random.randint(0, 1000) for p in range(0, 499)]
    while i <= 100:
        a, b = sequential_search(randmlst, -1)
        sum1 = sum1 + b
        i += 1
    seqavg=sum1/100

    randmlstsort = sorted(randmlst)
    while i <= 100:
        a, b = ordered_sequential_search(randmlstsort, -1)
        sum2 = sum2 + b
        i += 1
    ordavg=sum2/100

    while i <= 100:
        a, b = binary_search_iterative(randmlstsort, -1)
        sum3 = sum3 + b
        i += 1
    binitavg=sum3/100

    while i <= 100:
        a, b = binary_search_recursive(randmlstsort, -1)
        sum4 = sum4 + b
        i += 1
    binrecavg=sum4/100
    print("Sequential Search took %10.7f seconds to run, on average.\n" % seqavg,
          "Ordered Sequential Search took %10.7f seconds to run, on average.\n" % ordavg,
          "Binary Iterative Search took %10.7f seconds to run, on average.\n" % binitavg,
          "Binary Recursive Search took %10.7f seconds to run, on average.\n" % binrecavg)


if __name__ == __main__:
    main()
