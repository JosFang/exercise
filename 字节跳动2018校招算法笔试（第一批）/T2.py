def max_qujian(array):
    stack_num = []
    stack_summ = []
    array.append(-1)
    result = 0
    p = 0
    while p < len(array):
        summ = 0
        while stack_num and stack_num[-1] > array[p]:
            minn = stack_num.pop()
            summ = summ + minn + stack_summ.pop()
            result = max(result, summ*minn)
        stack_num.append(array[p])
        stack_summ.append(summ)
        p += 1
    return result

n = int(input())
array = [int(i) for i in input().strip().split()]
print(max_qujian(array))