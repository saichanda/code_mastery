"""
    Given an array a of size N which contains elements from 0 to N-1, 
    you need to find all the elements occurring more than once in the given array. 
    Return the answer in ascending order. If no such element is found, return list containing [-1]. 

    Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 
"""


class Solution:
    def duplicates(self, arr, n): 
        res = []
        for i in range(n):
            idx = arr[i] % n
            arr[idx] += n
        for i in range(n):
            if arr[i] // n >= 2:
                res.append(i)
        if not res:
            return [-1]
    	return res


if(__name__=='__main__'):
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter the list of elements between 0 and N-1: ").strip().split()))
    res = Solution().duplicates(arr, n)
    for i in res:
        print(i,end=" ")
