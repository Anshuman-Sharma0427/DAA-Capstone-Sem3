def merge_sort(parcels):
    """
    Sort parcels by delivery deadline using Merge Sort.
    Earliest deadline comes first.
    """

    # Base condition: a list with 0 or 1 element is already sorted
    if len(parcels) <= 1:
        return parcels

    # Find the middle position
    mid = len(parcels) // 2

    # Divide the list into two halves
    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """Combine two sorted lists into one sorted list."""

    result = []
    i = 0
    j = 0

    # Compare deadlines and select the earlier one
    while i < len(left) and j < len(right):

        if left[i]["deadline"] <= right[j]["deadline"]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from the left list
    result.extend(left[i:])

    # Add remaining elements from the right list
    result.extend(right[j:])

    return result
