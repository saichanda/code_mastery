"""
    Given an integer N and an integer D, rotate the binary representation
    of the integer N by D digits to the left as well as right and 
    return the results in their decimal representation after each of the rotation.
    Note: Integer N is stored using 16 bits. i.e. 12 will be stored as 0000000000001100.
"""


class Solution:
    def rotate(self, N, D):
        ar = [0] * 16
        if D > 16:
            D = D % 16
        i = len(ar) - 1
        while i >= 0:
            ar[i] = 1 if N % 2 != 0 else 0
            i -= 1
            N = int(N / 2)
            if not N:
                break
        res1 = sum(
            [2 ** (len(ar) - i - 1) * ele for i, ele in enumerate(ar[D:] + ar[:D])]
        )
        res2 = sum(
            [2 ** (len(ar) - i - 1) * ele for i, ele in enumerate(ar[-D:] + ar[:-D])]
        )
        return [res1, res2]


if __name__ == "__main__":
    n, d = input("Enter N and D values (separated by space)").strip().split(" ")
    n, d = int(n), int(d)
    ob = Solution()
    ans = ob.rotate(n, d)
    print(ans[0])
    print(ans[1])
