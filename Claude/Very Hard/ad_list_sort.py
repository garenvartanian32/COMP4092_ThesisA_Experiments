def advanced_sort(lst):
    odds  = sorted((x for x in lst if x % 2 != 0), reverse=True)
    evens = sorted(x for x in lst if x % 2 == 0)
    return odds + evens
 