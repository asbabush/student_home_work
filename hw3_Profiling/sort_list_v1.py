from memory_profiler import profile

sort_list_v1 = [100, 81, 3, 13, 211, 348, 7, 12, 43, 150, 200]


@profile
def sort_listv1():
    sort_list_v1.sort()
    return sort_list_v1


sort_listv1()
