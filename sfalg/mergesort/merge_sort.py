from merge_list import merge_list

def merge_sort(args):
    n = len(args)
    if n <= 1:
        return args
    else:
	left ,right = [],[]
	mid = n // 2
	left = args[:mid]
	right = args[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return list(merge_list(left,right))
     
            
