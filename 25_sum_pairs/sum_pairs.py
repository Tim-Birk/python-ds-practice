def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    i = 0
    for n1 in nums:
        j = i + 1
        for n2 in nums[j::1]:
            # this inner loop makes sure there is not a pair that sums to the goal before the outer loop number pairs
            for n3 in nums[j+1::1]:
                if n2 + n3 == goal:
                    return (n2, n3)
            if n1 + n2 == goal:
                return (n1, n2)
        i += 1
    return ()