# merged list of tuples from 2 lists
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = zip(a, b)
print(f"The merged list is {tuple(c)}")

# using zip, merge & range together
a = range(1, 8)
b = [11, 22, 33, 44, 55, 66, 77, 88]
c = zip(a, b)
print(f"The result is {tuple(c)}")

# sort the list
a = [100, 3637, 455, 12, 12, 1, 4, 12222]
ascending_order = sorted(a)
print(f"The sorted list is {ascending_order}")

# only odd numbers are passed to new list.
a = [1, 23, 3, 4, 5, 6, 7, 8, 9, 25, 26, 37]
b = list(filter(lambda x:(x%2!=0),a))
print(f"The new list is {b}")
