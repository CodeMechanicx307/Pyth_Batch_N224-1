"""
#problem-1 solution
def count_vowel_after_consonant(s):
    count = 0
    for start in range(len(s)-1):
        if s[start] not in 'aeiou' and s[start+1] in 'aeiou':
            count += 1
    return count

# main function
t = int(input())
for start in range(t):
    n = int(input())
    s = input()
    print(count_vowel_after_consonant(s))
"""


