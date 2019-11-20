# For a given integer N, print all the squares of integer numbers where the
# square is less than or equal to N, in ascending order.

x = int(input("Enter the number: "))
print("All the squares in the given range are:")
print([i**2 for i in range(1,x+1) if i**2 <= x])