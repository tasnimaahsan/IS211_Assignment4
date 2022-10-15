import time
import random

def insertion_sort(a_list):
    starttime=time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    endtime=time.time()
    executiontime=endtime-starttime
    return executiontime


def shell_sort(a_list):
    starttime=time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    endtime = time.time()
    executiontime = endtime - starttime
    return executiontime


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def main():
    i = 1
    suma = 0
    sumb = 0
    sumc = 0
    while i <= 100:
        lst500 = [random.randint(1, 1000) for p in range(0, 499)]
        lst1000 = [random.randint(1, 1000) for p in range(0, 999)]
        lst10000 = [random.randint(1, 1000) for p in range(0, 9999)]
        a = insertion_sort(lst500)
        b = insertion_sort(lst1000)
        c = insertion_sort(lst10000)
        suma += a
        sumb += b
        sumc += c
        i += 1
    inssuma = suma/100
    inssumb = sumb/100
    inssumc = sumc/100
    print("Insertion sort on 500 items took %10.7f seconds to run, on average.\n" % inssuma,
          "Insertion sort on 1000 items took %10.7f seconds to run, on average.\n" % inssumb,
          "Insertion sort on 10000 items took %10.7f seconds to run, on average.\n" % inssumc)
    k = 1
    sumd = 0
    sume = 0
    sumf = 0
    while k <= 100:
        alst500 = [random.randint(1, 1000) for p in range(0, 499)]
        alst1000 = [random.randint(1, 1000) for p in range(0, 999)]
        alst10000 = [random.randint(1, 1000) for p in range(0, 9999)]
        d = shell_sort(alst500)
        e = shell_sort(alst1000)
        f = shell_sort(alst10000)
        sumd += d
        sume += e
        sumf += f
        k += 1
    shellsumd = sumd/100
    shellsume = sume/100
    shellsumf = sumf/100
    print("Shell sort on 500 items took %10.7f seconds to run, on average.\n" % shellsumd,
          "Shell sort on 1000 items took %10.7f seconds to run, on average.\n" % shellsume,
          "Shell sort on 10000 items took %10.7f seconds to run, on average.\n" % shellsumf)


if __name__ == __main__:
    main()
