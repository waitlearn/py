def merge_list(left,right):
    merged_list = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged_list.append(left[left_idx])
            left_idx += 1
        else:
            merged_list.append(right[right_idx])
            right_idx += 1
    if left[left_idx:] != []:
        merged_list.extend(left[left_idx:])
    if right[right_idx:] != []:
        merged_list.extend(right[right_idx:])
    return merged_list

