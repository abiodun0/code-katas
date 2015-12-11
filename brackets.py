# Implement an algorithm to print all valid (e.g., properly opened and
# closed) combinations of n-pairs of parentheses.

# ```EXAMPLE:
# Input: 3 (e.g., 3 pairs of parentheses)
# Output: ()()(), ()(()), (())(), ((()))()


def printbrackets(p, i):
    if i < int(n):
        printbrackets(p+'()', i+1)
        printbrackets('('+p+')', i+1)
    else:
        print p


n = input("type the number of brackets you want to permutate: ")
printbrackets('()', 1)
