class Solution:
    def findLargest(self, N, S):
        ans = ""
        total = 0
        tmp = S
        if S == 0 and N > 1:
            return -1
        for _ in range(N):
            if S >= 9:
                S = S - 9
                ans += "9"
                total += 9
            else:
                ans += str(S)
                total += S
                break
        if len(ans) < N:
            for _ in range(N - len(ans)):
                ans += "0"

        return -1 if total != tmp else ans


if __name__ == "__main__":
    N = int(input("N: "))
    S = int(input("S: "))
    ob = Solution()
    res = ob.findLargest(N, S)
    if res != -1:
        print(f"Largest Number with {N} digits and summing up to {S} is {res}")
    else:
        print(f"There doesn't exist a number that has {N} digits and summing up to {S}")
