# Exercise 1
# Create a list L of numbers from 21 to 39
L=[i for i in range(21,40)]
# print the numbers of the list that are even
even=[]
for elem in L:
    if elem%2==0:
        even.append(elem)
print("The even elements of the list 'L' are {0}".format(even))
# print the numbers of the list that are multiples of 3
mult_3=[]
for elem in L:
    if elem%3==0:
        mult_3.append(elem)
print("The elements of the list 'L' multiples of 3 are {0}".format(mult_3))

# Exercise 2
# Print the last two elements of L 
print("The last two elements of the list 'L' are {0}".format(L[len(L)-2:]))

# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

L = ['1', '2', '3']
for i in range(10):
    if str(i) in L:
        print("'%d' is in the list"%i)
    else:
        print("'%d' not found"%i)
    
# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list
file=open('sprot_prot.fasta')
line=file.readline()
splitted=line.split('OS=')[1]
print("The second element of the resulting list is '%s'"%splitted)

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string

file = open('sprot_prot.fasta')
l = fh.readline()
' '.join(l.split('OS=')[1].split(' ')[0:2])
                      
                      
# Exercise 6
# reverse the string 'asor rosa'
                      
s = 'asor rosa'
s[::-1]         
                      
# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
                      
L.sort()
                      
# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
L_sorted = L
L_sorted.sort()                     
# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
def print_table():
    
    row1 = [2, 4]
    row2 = [3, 6]
    file = open('output_table.txt', 'w')
    file.write(' {} {} \n'.format(row1[0], row1[1]))
    file.write(' {} {} \n'.format(row2[0], row2[1]))
    
    
    file.close()
