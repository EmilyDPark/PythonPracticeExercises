# ---------------------------------------- Problem ----------------------------------------

# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.


# Constraints:

# 1 <= num <= 10^4
# num's digits are 6 or 9.



# ---------------------------------------- My Solution ----------------------------------------

# first instance of 6 in a number replaced with 9 will make it the biggest possible number with one change.

# example num
num = 9666

# Create necessary variable
times = -1

# Convert int into list with individual digits
b = str(num)
numlist = []
for i in b:
    numlist.append(int(i))

# Replace the first instance of 6 with 9
for i in numlist:
    times += 1
    if i == 6:
        del numlist[times]
        numlist.insert(times, 9)
        break

# Join the list to make an int
s = [str(i) for i in numlist]
maxnum = "".join(s)

print(maxnum)

# 28 ms <-- Beats 65.49%
# Solved February 4, 2020



# ---------------------------------------- 8 ms Solution on LeetCode ----------------------------------------

class Solution:
    def maximum69Number (self, num: int) -> int:
        max_val = num
        length = len(str(num))
        for i in range(length):
            temp = list(str(num))
            temp[i] = '9'
            max_val = max(max_val, int(''.join(temp)))
        return max_val