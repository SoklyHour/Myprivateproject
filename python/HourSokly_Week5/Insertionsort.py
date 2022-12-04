def insertion_sort(num):
    for i in range(1, len(num)):
        j = i
        while num[j-1] > num[j] and j > 0:
            num[j-1], num[j] = num[j], num[j-1]
            j -= 1

num = [1,3,5,6,8,9, -1,-20,100,76]
insertion_sort(num)
print(num)