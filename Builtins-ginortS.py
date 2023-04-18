# You are given a string S. 

# S contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Input Format

# A single line of input contains the string S.

# Output Format

# Output the sorted string S.

# Sample Input

# Sorting1234

# Sample Output

# ginortS1324



S = input()

sort = sorted(S, key= lambda x : (x.isdigit(), x.isupper(), x.islower(), x in '02468', x))

print(''.join(sort))