def merge_sort(list): 
    """
    Sorts list in ascending order
    Returns a new sorted list

    Divide: Finds the midpoint of list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Conquer: Merge the sorted sublists created in the previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)            # recursive portion of the function
    right = merge_sort(right_half)          # recursive portion of the function

    return merge(left, right)

    def split(list): 
        """
        divide the unsorted list at midpoint into two sublists
        Return two sublists -- left and right
        """
        mid = len(list) // 2 
        left = list[:mid]
        right = list[mid:]
        return left, right