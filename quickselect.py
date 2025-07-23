import random

def quickselect(arr, k):
    """
    Finds the k-th smallest element in an unsorted list (0-indexed).
    e.g., k = 0 finds the minimum element, k = len(arr)-1 finds the maximum.
    
    Time Complexity:
        Average: O(n)
        Worst: O(n^2)
    Space Complexity: O(1) auxiliary space (tail-recursive / iterative)
    """
    if not arr or k < 0 or k >= len(arr):
        raise ValueError("Index k out of bounds or empty array.")
        
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if left == right:
            return arr[left]
            
        # Select a random pivot index and partition the array
        pivot_idx = random.randint(left, right)
        pivot_new_idx = _partition(arr, left, right, pivot_idx)
        
        if k == pivot_new_idx:
            return arr[k]
        elif k < pivot_new_idx:
            right = pivot_new_idx - 1
        else:
            left = pivot_new_idx + 1

def _partition(arr, left, right, pivot_idx):
    """
    Partitions the array around the pivot element.
    Moves all elements smaller than pivot to its left and larger to its right.
    """
    pivot_val = arr[pivot_idx]
    # Move pivot to the end
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store_idx = left
    
    for i in range(left, right):
        if arr[i] < pivot_val:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1
            
    # Move pivot to its final place
    arr[right], arr[store_idx] = arr[store_idx], arr[right]
    return store_idx


if __name__ == "__main__":
    print("Running Quickselect tests...")
    
    # Test Case 1: Standard array
    nums1 = [3, 2, 1, 5, 4, 6]
    # Sorted: [1, 2, 3, 4, 5, 6]
    assert quickselect(list(nums1), 0) == 1, "Failed min element"
    assert quickselect(list(nums1), 3) == 4, "Failed median element"
    assert quickselect(list(nums1), 5) == 6, "Failed max element"
    
    # Test Case 2: Array with duplicate elements
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # Sorted: [1, 2, 2, 3, 3, 4, 5, 5, 6]
    assert quickselect(list(nums2), 4) == 3, "Failed with duplicates"
    
    # Test Case 3: Single element array
    assert quickselect([42], 0) == 42
    
    # Test Case 4: Already sorted array
    nums4 = [10, 20, 30, 40, 50]
    assert quickselect(list(nums4), 2) == 30
    
    print("All Quickselect tests passed successfully!")
