#Print an array of the elements that do not sum to n=3.

#Input Format
#Four integers x, y, z and n, each on a separate line.

#Constraints
#Print the list in lexicographic increasing order.

x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])