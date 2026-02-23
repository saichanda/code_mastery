# Date : 31/01/26
# Day : Saturday
# Topic : Edit Distance

def solve(dp, word1, word2, i, j):
    # Base cases: if one string is empty, we need 
    # the number of operations equal to the length of the other string
    if i == 0: return j
    if j == 0: return i

    # Check memoization table
    if dp[i][j] != -1:
        return dp[i][j]

    # If characters match, no operation needed for this step
    if word1[i-1] == word2[j-1]:
        dp[i][j] = solve(dp, word1, word2, i-1, j-1)
    else:
        # Otherwise, consider Replace, Delete, and Insert
        replace = solve(dp, word1, word2, i-1, j-1)
        delete  = solve(dp, word1, word2, i-1, j)
        insert  = solve(dp, word1, word2, i, j-1)
        
        dp[i][j] = 1 + min(replace, delete, insert)

    return dp[i][j]

def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    # Initialize a 2D list with -1 for memoization
    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    return solve(dp, word1, word2, m, n)

# --- Main Function ---
if __name__ == "__main__":
    # Example input
    s1 = "horse"
    s2 = "ros"
    
    result = min_distance(s1, s2)
    
    print(f"Word 1: '{s1}'")
    print(f"Word 2: '{s2}'")
    print(f"Minimum Edit Distance: {result}")

# this code calculates the minimum edit distance between two words using a recursive approach with memoization.