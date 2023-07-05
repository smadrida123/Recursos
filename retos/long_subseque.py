#Finding the longest increasing subsequence: You need to write a function that takes a list of integers as input and returns the longest 
#increasing subsequence within that list. An increasing subsequence is a sequence of elements that are in ascending order but not necessarily 
#contiguous.
def longest_increasing_subsequence(nums):
    n = len(nums)
    if n == 0:
        return []

    # Initialize an array to store the lengths of the longest increasing subsequences
    lengths = [1] * n

    # Initialize an array to store the previous indices of the elements in the subsequences
    prev_indices = [-1] * n

    # Traverse the list and update the lengths and prev_indices arrays
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j

    # Find the index of the longest subsequence
    max_length = max(lengths)
    max_index = lengths.index(max_length)

    # Reconstruct the longest increasing subsequence
    subsequence = []
    while max_index != -1:
        subsequence.append(nums[max_index])
        max_index = prev_indices[max_index]

    # Reverse the subsequence to get the correct order
    subsequence.reverse()

    return subsequence

nums = [3, 10, 2, 1, 20]
result = longest_increasing_subsequence(nums)
print(result)  # Output: [3, 10, 20]

