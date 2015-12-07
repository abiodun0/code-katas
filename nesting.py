# A string S consisting of N characters is called properly nested if:

# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.

# Write a function:

# int solution(char *S);

# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

# Assume that:

# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".
# Complexity:


def solution(S):
    total = 0
    for i in range(0,len(S)):
        j = 1 if S[i] is "(" else -1
        total += j
        if total is -1:
            return 0
    if total != 0:
        return 0
    return 1