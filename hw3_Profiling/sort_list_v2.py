from memory_profiler import profile

sort_list_v2 = [100, 81, 3, 13, 211, 348, 7, 12, 43, 150, 200]
sorted_list = []


@profile
def sort_listv2():
    for i in range(0, len(sort_list_v2)):
        sorted_list.append(min(sort_list_v2))
        sort_list_v2.remove(min(sort_list_v2))
    return sorted_list


sort_listv2()
