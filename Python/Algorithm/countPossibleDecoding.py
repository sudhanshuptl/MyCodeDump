# Count Possible Decodings of a given Digit Sequence
# Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings
#  of the given digit sequence.
# Input:  digits[] = "121"
# Output: 3
# // The possible decodings are "ABA", "AU", "LA"
#
# Input: digits[] = "1234"
# Output: 3
# // The possible decodings are "ABCD", "LCD", "AWD"


def recursive_count(digits, n):
    # base case when size of digit string is 0 or 1
    if n <= 1:
        return 1
    count = 0
    # Processing data from end to start
    # if digit > 0 means can be a character count it
    if digits[n-1] > '0':
        count = recursive_count(digits, n-1)
    # if two digits is in out range of valid character encoding
    if digits[n-2:n] < '27':
        count += recursive_count(digits, n-2)

    return count


def dynamic_count_possibilities(digits, n):
    # Solving issue with dynamic programming
    count = [0]*(n+1)
    # base case when 0 or 1 character
    count[0], count[1] = 1, 1

    for i in range(2, n+1):
        count[i] = 0
        # If the last digit is not 0,
        # then last digit must add to
        # the number of words
        if digits[i-1] > '0':
            count[i] = count[i-1]

        # If second last digit is smaller than 27
        if digits[i-2:i] < '27':
            count[i] += count[i-2]
    return count[n]


if __name__ == '__main__':
    digits='1228'
    print('total decode possibilities :',recursive_count(digits, len(digits)))
    print('using dynamic programming ', dynamic_count_possibilities(digits, len(digits)))


