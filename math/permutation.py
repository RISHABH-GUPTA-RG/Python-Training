# A Python program to print all
# permutations using library function
from itertools import permutations

perm = permutations(['r', 'i', 's', 'h', 'a', 'b', 'h'])

a=0

# Print the obtained permutations
for i in list(perm):
    print(i,a)
    a=a+1	

input()