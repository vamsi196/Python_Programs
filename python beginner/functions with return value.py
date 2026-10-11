import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
print(mean_median_mode([3,5,45,3,2,1,89]))