"""
    Given a sorted array arr containing n elements with possibly duplicate
    is to find indexes of first elements, the task is to find the first and
    last occurrences of an element x in the given array.

    Returns:
        int: first index of the element x
        int: last index of the element x
"""


class Solution:
    def find(self, arr, n, x):
        if x not in arr:
            return -1, -1
        first = 0
        last = n - 1
        for _ in range(n):
            if arr[first] == x and arr[last] == x:
                break
            if arr[first] != x:
                first += 1
            if arr[last] != x:
                last -= 1
        return first, last


l = list(map(int, input("Enter n and x: ").split()))
n = l[0]
x = l[1]
arr = list(map(int, input(f"Enter list of {n} elements:\n").split()))
ob = Solution()
ans = ob.find(arr, n, x)
print(*ans)
