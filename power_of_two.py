class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        flag = True
        if n == 0:
            return 0
        if n == 1:
            return 1
        while n > 1:
            if n == 2:
                return 1
            if n % 2 == 0:
                n = n / 2
                continue
            else:
                flag = False
                break
        return 0 if not flag or n == 1 else 1


if __name__ == "__main__":
    n = int(input("Enter the integer n: "))
    ob = Solution()
    if ob.isPowerofTwo(n):
        print(f"YES, {n} can be written in powers of 2")
    else:
        print(f"NO, {n} cannot be written as powers of 2")
