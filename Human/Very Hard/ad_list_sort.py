def advanced_sort(lst):
	returned_list = []
	set_item = []
	for item in lst:
		if item in set_item:
			continue
		temporary_list = []
		for a in range(lst.count(item)):
			temporary_list.append(item)
		returned_list.append(temporary_list)
		set_item.append(item)
	return returned_list