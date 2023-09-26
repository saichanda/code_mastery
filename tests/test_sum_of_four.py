"""
    Given an array A of integers and another number K.
    Find all the unique quadruple from the given array that sums up to K.

    Also note that all the quadruples which you return should be internally sorted,
    i.e., for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.
"""



from itertools import combinations


class Solution:
    # def fourSum(self, arr, k):
    #     res = set()
    #     sublist_combo = list(set(combinations(arr, 4)))
    #     for sub_list in set(sublist_combo):
    #         if sum(sub_list) == k:
    #             sub_list = list(sub_list)
    #             sub_list.sort()
    #             res.add(tuple(sub_list))
    #     res = list(res)
    #     res.sort()
    #     return res

    # def fourSum(self, arr, k):
    #     # Generate unique combinations of 4 elements
    #     sublist_combos = set(combinations(arr, 4))

    #     # Initialize a set to store unique results
    #     results = set()

    #     for sub_list in sublist_combos:
    #         if sum(sub_list) == k:
    #             results.add(tuple(sorted(sub_list)))

    #     return sorted(list(results))
    
    def fourSum(self, arr, k):
        arr.sort()
        n = len(arr)
        results = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left = j + 1
                right = n - 1

                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == k:
                        results.add((arr[i], arr[j], arr[left], arr[right]))
                        left += 1
                        right -= 1
                    elif total < k:
                        left += 1
                    else:
                        right -= 1

        return sorted(list(results))


if __name__=='__main__':
    n, k=map(int,input("Enter N & K: ").split())
    a=list(map(int,input(f"Enter the list of {N} elements: ").strip().split()))[:n]
    ob=Solution().fourSum(a, k)
    print("[")
    for v in ans:
        for u in v:
            print(u, end=" ")
        print("],[", end="")
    print("]")
    if(len(ans)==0):
        print(-1, end="")
    print()
